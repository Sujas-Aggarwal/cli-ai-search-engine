from click import style,echo
class CLI:
    def format_html(self, html):
        """
        This function is to style html text into a string which can be displyed in cli with proper format.
        """
        formatted_string = style(html)
        return formatted_string
    def line_break():
        echo("\n")