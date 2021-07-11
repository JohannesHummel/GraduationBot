from habanero import Crossref

def paper_search(topic):
   # my_dict = {"title":[],"doi":[]}
    cr = Crossref()
    x = cr.works(query = topic, limit = 3)
    final_string = ""
    for z in x['message']['items']:
        final_string += f"{z['title']}: {z['URL']} \n"

    return final_string