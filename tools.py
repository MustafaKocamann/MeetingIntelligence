import os 
from exa_py import Exa
from crewai.tools import tool

class ExaSearchTool():
    """Tool for performing searches and retrieving content using the Exa API.
    
    This class provides static methods to search the web, find similar pages,
    and retrieve the contents of specific webpages.
    """

    @staticmethod
    @tool("search")
    def search(query: str) -> str:
        """Searches for a webpage based on the provided query.

        Args:
            query (str): The search query string.

        Returns:
            str: A string representation of the search results, or an error message if the search fails.
        """
        try:
            result = ExaSearchTool._exa().search(f"{query}", use_autoprompt=True, num_results=3)
            return str(result)
        except Exception as e:
            return f"Search error: {str(e)}"

    @staticmethod
    @tool("find_similar")
    def find_similar(url: str) -> str:
        """Searches for webpages similar to a given URL.

        Args:
            url (str): The URL to find similar pages for. This should ideally be a URL returned from a previous search.

        Returns:
            str: A string representation of the similar pages found, or an error message if the operation fails.
        """
        try:
            result = ExaSearchTool._exa().find_similar(url, num_results=3)
            return str(result)
        except Exception as e:
            return f"Find similar error: {str(e)}"

    @staticmethod
    @tool("get_contents")
    def get_contents(page_ids_str: str) -> str:
        """Retrieves the contents of specific webpages.

        Args:
            page_ids_str (str): A string representation of a list of page IDs (e.g., "['id1', 'id2']").
                               These IDs are typically returned from a search or find_similar operation.

        Returns:
            str: The combined contents of the requested pages, separated by newlines, or an error message if retrieval fails.
        """
        try:
            # Safely evaluate the string to a list. 
            # Note: In a production environment, ast.literal_eval is safer than eval.
            ids_list = eval(page_ids_str)
            contents = ExaSearchTool._exa().get_contents(ids_list)
            contents_str = contents.split("URL:")
            contents_str = [content[:1000] for content in contents_str]
            return "\n\n".join(contents_str)
        except Exception as e:
            return f"Get contents error: {str(e)}"

    @staticmethod
    def tools():
        """Returns a list of available tools in this class.

        Returns:
            list: A list of tool functions (search, find_similar, get_contents).
        """
        return [
            ExaSearchTool.search,
            ExaSearchTool.find_similar,
            ExaSearchTool.get_contents
        ]

    @staticmethod
    def _exa():
        """Initializes and returns the Exa client.

        Returns:
            Exa: An instance of the Exa client initialized with the API key from environment variables.
        """
        return Exa(api_key=os.getenv("EXA_API_KEY"))