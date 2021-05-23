import requests
import re
nigger_finder_pattern_1 = r"Showing.+of.(\d)"
nigger_finder_pattern_2 = r'<span.+\n.+<a.+(\/view_video.php.+)".title'
nigger_finder_pattern_3 = r'<span.+\n.+title="(.+)".class'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
def main():
    print(f"{'='*  19}\nLOOKING FOR NIGGERS\n{'='* 19}")
    nigger_text = requests.get("https://www.pornhub.com/video/search?search=black+girl",headers=headers).text
    result = re.findall(nigger_finder_pattern_1,nigger_text)
    print(f"AMOUNT OF NIGGER VIDEOS {result[0]})")
    print("="*19)
    nigger_url = re.findall(nigger_finder_pattern_2,nigger_text)
    nigger_name = re.findall(nigger_finder_pattern_3,nigger_text)
    for i in range(0,len(nigger_url)):
        print(f"Nigger video url {nigger_url[i]}")
        print(f"Nigger video name {nigger_name[i]}")
if __name__ == "__main__":
    main()
