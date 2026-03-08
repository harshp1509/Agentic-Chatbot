from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        if not self.config.read(config_file):
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

    def get_llm_options(self):
        options_str = self.config["DEFAULT"].get("LLM_OPTIONS", "")
        return [opt.strip() for opt in options_str.split(',') if opt.strip()]
    
    def get_usecase_options(self):
        options_str = self.config["DEFAULT"].get("USECASE_OPTIONS", "")
        return [opt.strip() for opt in options_str.split(',') if opt.strip()]
    
    def get_groq_model_options(self):
        options_str = self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS", "")
        return [opt.strip() for opt in options_str.split(',') if opt.strip()]
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "LangGraph AgenticAI")