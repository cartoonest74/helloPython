class Billboard:
    ranking = 0
    title = ''
    singer = ''
    def __init__(self,tag):
        title_path ='li:last-child>ul>li:first-child>h3.c-title'
        singer_path ='li:last-child>ul>li:first-child>span.c-label'
        ranking_path ='li:first-child>span:first-child.c-label'
        self.title = self.get_text(tag,title_path)
        self.singer = self.get_text(tag,singer_path)
        self.ranking = self.get_text(tag,ranking_path)
    
    def get_text(self, parent_tag, selector):
        tag = self.get_tag(parent_tag, selector)
        trans_text = tag.text.strip()
        return trans_text

    def get_tag(self, parent_tag, selector):
        tag = parent_tag.select_one(selector)
        if tag:
            return tag

    def __str__(self):
        return self.to_str()
        
    def to_str(self):
        return '{}\t{}\t{}'.format(self.ranking, self.title, self.singer)
