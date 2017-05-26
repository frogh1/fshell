# -*- coding: utf-8 -*-

# project: fshell
# author: s0nnet
# time: 2017-05-14
# desc: web_viewset_样本库管理_danfunc


from view_base import *

from fsm_lib_danfunc import *


class ViewLibDanfunc(ViewBase):

    def GET(self):
        bRet, sRet = self.check_login()
        if not bRet:
            Log.err("not login!")
            return web.seeother("/login")

        render=web.template.frender("templates/lib-danfunc.html")
        return render()

    def POST(self):
        return self.GET()



class ViewLibDanfuncList(ViewBase):

    def __init__(self):
        self._rDict = {
            "page": {'n': 'page', 't': int, 'v': 1},
            "count": {'n': 'count', 't': int, 'v': 10}
        }

    def _check_param(self):

        if not self.page: return False, "param(page) is None!"
        if not self.count: return False, "param(count) is None!"

        return True, None

    def _deal_lib_danfunc_list_get(self):
        bRet, userId = FsmUser.get_user_id(self.get_user_name())
        if not bRet:
            Log.err("username: %s not bussiness" % (self.get_user_name()))
            return bRet, userId

        bRet, sRet = FsmLibDanfunc.lib_danfunc_list(userId, self.page, self.count)
        if not bRet:
            return False, sRet

        return True, sRet

    def GET(self):
        if not self.check_login():
            return self.make_error("user not login")
        bRet, sRet = self.process(self._deal_lib_danfunc_list_get)
        if not bRet:
            Log.err("deal_lib_danfunc_list_get: %s" % (str(sRet)))
            return self.make_error(sRet)

        return self.make_response(sRet)
