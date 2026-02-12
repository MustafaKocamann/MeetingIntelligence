from textwrap import dedent 
from crewai import Task 

class MeetingPrepTasks():
    """Defines the tasks for the Meeting Preparation Crew.
    
    This class contains methods to create specific tasks such as research,
    industry analysis, meeting strategy, and briefing summaries.
    """

    def research_task(self, assigned_agent, meeting_participants, meeting_context):
        """Creates a task for researching meeting participants and companies.

        Args:
            assigned_agent (Agent): The agent assigned to perform this task.
            meeting_participants (str): A string listing the emails or names of the meeting participants.
            meeting_context (str): A description of the meeting's context.

        Returns:
            Task: A CrewAI Task object configured for research.
        """
        return Task(
            description = dedent(f"""\
                Conduct comprehensive research on each of the individuals and companies
                involved in the upcoming meeting. Gather information on recent 
                news, achievements, professional background, and any relevant 
                business activities.

                Participants: {meeting_participants}
                Meeting Context: {meeting_context}"""),
            expected_output = dedent(f"""\
              A detailed report summarizing key findings about each participant
              and company, highlighting information that could be relevant for the meeting."""),
            agent = assigned_agent,
            async_execution = True
        )

    def industry_analysis_task(self, assigned_agent, meeting_participants, meeting_context):
        """Creates a task for analyzing industry trends and opportunities.

        Args:
            assigned_agent (Agent): The agent assigned to perform this task.
            meeting_participants (str): A string listing the emails or names of the meeting participants.
            meeting_context (str): A description of the meeting's context.

        Returns:
            Task: A CrewAI Task object configured for industry analysis.
        """
        return Task(
            description = dedent(f"""\
              Analyze the current industry trends, challenges, and opportunities
              relevant to the meeting's context. Consider market reports, recent
              developments, and expert opinions to provide a comprehensive 
              overview of the industry landscape.

              Participants: {meeting_participants}
              Meeting Context: {meeting_context}"""),

            expected_output = dedent("""\
              An insightful analysis that identifies major trends, potential
              challenges, and strategic opportunities."""),
            async_execution = True,
            agent = assigned_agent
            
        )

    def meeting_strategy_task(self, assigned_agent, meeting_context, meeting_objective):
        """Creates a task for developing a meeting strategy.

        Args:
            assigned_agent (Agent): The agent assigned to perform this task.
            meeting_context (str): A description of the meeting's context.
            meeting_objective (str): The specific objective or goal of the meeting.

        Returns:
            Task: A CrewAI Task object configured for meeting strategy development.
        """
        return Task(
            description = dedent(f"""\
                Develop strategic talking points, questions, and discussion angles
                for the meeting based on the research and industry analysis conducted

                Meeting Context: {meeting_context}
                Meeting Objective: {meeting_objective}"""),
            expected_output = dedent("""\
                Complete report with a list of key talking points, strategic questions 
                to ask to help achieve the meetings objective during the meeting."""),
            agent = assigned_agent
            )
        
    def summary_and_briefing_task(self, assigned_agent, meeting_context, meeting_objective):
        """Creates a task for compiling a final briefing document.

        Args:
            assigned_agent (Agent): The agent assigned to perform this task.
            meeting_context (str): A description of the meeting's context.
            meeting_objective (str): The specific objective or goal of the meeting.

        Returns:
            Task: A CrewAI Task object configured for summary and briefing.
        """
        return Task(
            description = dedent(f"""\
                Compile all the research findings, industry analysis, and strategic
                talking points into a concise, comprehensive briefing document for
                the meeting.
                Ensure the briefing is easy to digest and equips the meeting 
                participants with all necessary information and strategies.

                Meeting Context: {meeting_context}
                Meeting Objective: {meeting_objective}"""),
            expected_output = dedent("""\
                A well-structured briefing document that includes sections for
                participant bios, industry overview, talking points, and strategic recommendations."""),
            agent = assigned_agent
            )
        
        
        
              
          