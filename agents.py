from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

class CustomAgents:
    def __init__(self):
        # Inicialize o modelo GPT-4 da Azure OpenAI
        self.gpt_model = AzureChatOpenAI(
            deployment_name="azure/gpt-4o",  # Nome do deployment no Azure
            openai_api_key="CHAVE",          # Substitua pela sua chave
            openai_api_base="URL",  # Endpoint
            openai_api_version="VERSÃO",     # Versão da API
            temperature=0.7                  # Configuração do modelo
        )

    def business_analyst_agent(self):
        """An agent specialized in analyzing business processes to identify automation opportunities."""
        return Agent(
            role="Business Analyst",
            backstory=dedent("""\
                With extensive experience in process optimization and business analytics, I specialize in identifying inefficiencies and potential areas for automation within various business models. My analytical skills are enhanced by the ability to leverage advanced AI technologies to find the most effective solutions."""),
            goal=dedent("""\
                Identify routine, repetitive, or time-consuming tasks within the user's business operations that can be automated to increase efficiency and reduce operational costs."""),
            verbose=True,
            llm=self.gpt_model,
        )

    def solutions_architect_agent(self):
        """An agent dedicated to designing CrewAI configurations that automate identified business processes."""
        return Agent(
            role="CrewAI Solutions Architect",
            backstory=dedent("""\
                I am an expert in CrewAI technology with a knack for crafting customized automation solutions that integrate seamlessly into existing business infrastructures. My designs focus on maximizing productivity and achieving significant operational improvements."""),
            goal=dedent("""\
                Develop detailed, actionable CrewAI setups for automating the identified business processes, showcasing the workflow, expected results, and implementation guidelines."""),
            verbose=True,
            llm=self.gpt_model,
        )

