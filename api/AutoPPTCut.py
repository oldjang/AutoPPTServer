class Server():
    def getLogicCut(self, file_path: str, cut_num: int):
        logic_cut = ["1","2"]
        summary = ["1","2"]
        return logic_cut, summary

    def getDisplayCut(self, logic_cut_list: list, expect_page_num: int):
        rst = [[]]
        return rst

    def makePPT(self, logic_cut, display_cut, expect_page_num, title, template_path, dst_name) -> bool:
        return True