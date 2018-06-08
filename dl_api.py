import requests
def dl(filename):
    url='https://raw.githubusercontent.com/frozenzj/d2_analysis_learning/master/{}'.format(filename)
    r=requests.get(url)
    with open(filename,'wb') as f:
        f.write(r.content)
    f.close()
