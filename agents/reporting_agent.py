"""
Reporting Agent

This agent replicates and extends the functionality of the main reporting agent
with specialized capabilities for generating DFIR HTML reports.
"""

import os
from openai import AsyncOpenAI
from cai.sdk.agents import Agent, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
from pathlib import Path

# Import tools from CAI framework
try:
    from cai.tools.reconnaissance.generic_linux_command import generic_linux_command
    from cai.tools.reconnaissance.exec_code import execute_code
except ImportError:
    # Fallback simple implementations if CAI tools not available
    @function_tool
    def generic_linux_command(command: str) -> str:
        """Execute a Linux command"""
        import subprocess
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return f"Exit code: {result.returncode}\nStdout: {result.stdout}\nStderr: {result.stderr}"
        except Exception as e:
            return f"Error executing command: {str(e)}"
    
    @function_tool 
    def execute_code(code: str, language: str = "python") -> str:
        """Execute code"""
        return f"Code execution simulated for: {code[:100]}..."

load_dotenv()

def _load_system_prompt(prompt_file: str) -> str:
    """
    Load system prompt from agents/prompts/ directory
    
    Args:
        prompt_file: Name of the prompt file (e.g., 'system_reporting_agent.md')
        
    Returns:
        str: Content of the prompt file
    """
    prompt_path = Path(__file__).parent / "prompts" / prompt_file
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠️  Warning: Prompt file {prompt_file} not found at {prompt_path}")
        print(f"   Using fallback prompt")
        return ""
    except Exception as e:
        print(f"⚠️  Error loading prompt file {prompt_file}: {e}")
        return ""

@function_tool
def get_html_template() -> str:
    """Get the HTML template for DFIR reports"""
    try:
        template_path = Path(__file__).parent.parent / "html_report_template.html"
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error loading HTML template: {str(e)}"

def create_reporting_agent() -> Agent:
    """
    Create and configure the reporting agent
    
    Returns:
        Agent: Configured reporting agent
    """
    
    # Define tools for the reporting agent
    tools = [
        generic_linux_command,
        execute_code,
        get_html_template,
    ]
    
    # Configure model client more explicitly
    model_name = os.getenv("CAI_MODEL", "alias1")
    
    print(f"🤖 Configuring Reporting agent with model: {model_name}")
    
    # Create model client based on configuration
    if model_name.lower() == "ollama":
        # Use Ollama local instance
        ollama_base_url = os.getenv("OLLAMA_API_BASE", "http://localhost:11434/v1")
        ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
        print(f"✅ Using Ollama configuration: {ollama_base_url} with model {ollama_model}")
        openai_client = AsyncOpenAI(
            base_url=ollama_base_url,
            api_key=os.getenv("OLLAMA_API_KEY", "ollama")
        )
        # Override model name to use the Ollama model
        model_name = ollama_model
    elif "alias" in model_name.lower():
        print("✅ Using Alias model configuration")
        print(f"🔍 ALIAS_API_KEY configured: {'✅' if os.getenv('ALIAS_API_KEY') else '❌'}")
        openai_client = AsyncOpenAI()  # CAI handles Alias routing automatically
    else:
        print("✅ Using standard OpenAI/external API configuration")
        # Support custom API base URL for external endpoints
        api_base = os.getenv("OPENAI_API_BASE")
        api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ALIAS_API_KEY")
        if api_base:
            print(f"   Using custom API base: {api_base}")
            openai_client = AsyncOpenAI(base_url=api_base, api_key=api_key)
        else:
            openai_client = AsyncOpenAI(api_key=api_key)
    
    # Add input and output path files to system prompt
    system_prompt = _load_system_prompt("system_reporting_agent.md")
    system_prompt += f"\n\nInput path: latest file in logs directory"
    system_prompt += f"\nOutput path: dfir_reports/dfir_report.html"

    # Create the agent
    reporting_agent = Agent(
        name="DFIR Reporting Agent",
        instructions=system_prompt,
        description="""Specialized agent for generating professional HTML reports from DFIR analysis.
                       Expert in transforming technical forensic data into comprehensive,
                       visually appealing reports for stakeholders.""",
        model=OpenAIChatCompletionsModel(
            model=model_name,
            openai_client=openai_client,
        ),
        tools=tools,
    )
    
    return reporting_agent
