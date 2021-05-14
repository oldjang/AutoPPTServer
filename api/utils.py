class Information:
    def __init__(self, title, page_num, cut_num, template_id, file_url):
        self.title = title
        self.page_num = page_num
        self.cut_num = cut_num
        self.template_id = template_id
        self.file_url = file_url
        self.summary = []

    def to_dict(self):
        return {
            'title': self.title,
            'page_num': self.page_num,
            'cut_num': self.cut_num,
            'template_id': self.template_id,
            'file_url': self.file_url,
            'summary': self.summary
        }

    def set_logic_cut(self, cut_num, list1, list2):
        for i in range(cut_num):
            self.summary.append({"name": list2[i], "heading": list1[i]})

    def get_logic_cut(self):
        logic_cut_list = []
        summary = []
        for info in self.summary:
            logic_cut_list.append(info["heading"])
            summary.append(info["name"])

        return logic_cut_list, summary


class InformationStore:
    def __init__(self):
        self.data = {}

    def save(self, name, information):
        self.data[name] = information

    def get(self, name):
        return self.data[name]
