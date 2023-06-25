from grocer_app.utils import get_requests_url_html

class TestGetRequests():

    def test_negative_response(self):
        # Where to navigate
        baseurl = 'https://www.checkers.co.za/c-2256/All-Departments?q=%3Arelevance%3AbrowseAllStoresFacetOff%3AbrowseAllStoresFacetOff&page=0'
        # laat requests soos browser lyk en nie python
        user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'}
        test_url_html = get_requests_url_html(baseurl=baseurl, user_agent=user_agent)
        assert test_url_html != "Dummy Incorrect Response"



"""
def get_requests_url_html(baseurl = None, user_agent = None):

    Definition: this function parses the url_html value that is needed to find product name.
    ----------
    Inputs:
    baseurl: str
    user_agent: dict
    ----------
    Returns:
    url_html: (MORNE ASB VUL IN, ek het nie context oor wat presies BeautifulSoup doen nie)
 
    requests = requests.get(baseurl, headers= user_agent).text
    url_html = BeautifulSoup(requests,'html.parser')
    return url_html


"""

