from textwrap import dedent 
from crewai import Agent, LLM
from tools import ExaSearchTool

class MeetingPrepAgents():
    """Defines the agents for the Meeting Preparation Crew.

    This class provides methods to create specialized agents for research,
    industry analysis, strategy development, and briefing coordination.
    """

    def research_agent(self):
        """Creates a Research Specialist agent.

        Returns:
            Agent: A CrewAI Agent configured to conduct research using ExaSearchTool.
        """
        return Agent(
            role = "Research Specialist",
            goal = "Conduct thorough research on people and companies involved in the meeting",
            tools = ExaSearchTool.tools(),
            llm = LLM(model="groq/llama-3.3-70b-versatile"),
            backstory = dedent("""\
                As a Research Specialist, your mission is to uncover detailed information 
                about the individuals and entities participating in the meeting. Your insights
                will lay the groundwork for strategic meeting preparation.""" ),
            verbose = True
        )

    def industry_analysis_agent(self):
        """Creates an Industry Analyst agent.

        Returns:
            Agent: A CrewAI Agent configured to analyze industry trends using ExaSearchTool.
        """
        return Agent(
            role = "Industry Analyst",
            goal = "Analyze the current industry trends, challenges, and opportunities",
            tools = ExaSearchTool.tools(),
            llm = LLM(model="groq/llama-3.3-70b-versatile"),
            backstory = dedent("""\
                As an Industry Analyst, your analysis will identify key trends,
                challenges facing the industry, and potential opportunities that
                could be leveraged during the meeting for strategic advantage."""),
            verbose = True
        )

    def meeting_strategy_agent(self):
        """Creates a Meeting Strategy Advisor agent.

        Returns:
            Agent: A CrewAI Agent configured to develop meeting strategies.
        """
        return Agent(
            role = "Meeting Strategy Advisor",
            goal = "Develop talking points, questions, and strategic angles for the meeting",
            llm = LLM(model="groq/llama-3.3-70b-versatile"),
            backstory = dedent("""\
                As a Strategy Advisor, your expertise will guide the development of
                talking points, insightful questions, and strategic angles
                to ensure the meeting's objectives are achieved.""" ),
            verbose = True
        )

    def summary_and_briefing_agent(self):
        """Creates a Briefing Coordinator agent.

        Returns:
            Agent: A CrewAI Agent configured to compile briefing documents.
        """
        return Agent(
            role = "Briefing Coordinator",
            goal = "Compile all gathered information into a concise briefing document",
            llm = LLM(model="groq/llama-3.3-70b-versatile"),
            backstory = dedent("""\
                As the Briefing Coordinator, your role is to synthesize the research,
                analysis, and strategic points into a clear, actionable briefing
                for the meeting participants."""),
            verbose = True
        )