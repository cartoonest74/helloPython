class Bilbord:
    ranking = 0
    title = ''
    singer = ''
    category = ''
    def __init__(self, tag):
        ranking_root = 'li:first-child>span:first-child.c-label'
        title_root = 'li:last-child>ul>li:first-child>h3.c-title'
        singer_root = 'li:last-child>ul>li:first-child>span.c-label'
        self.ranking = self.get_text(tag, ranking_root)
        self.title = self.get_text(tag, title_root)
        self.singer = self.get_text(tag, singer_root)

    def get_text(self,parent_tag, selector):
        tag  = self.get_tag(parent_tag, selector)
        return tag.text.strip()

    def get_tag(self,parent_tag, selector):
        tags = parent_tag.select_one(selector)
        if  tags:
            return tags

    def __str__(self):
        return self.to_str()
        
    def to_str(self):
        return '{}\t{}\t{}'.format(self.ranking, self.title, self.singer)
