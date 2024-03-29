#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/13 16:05
# @Author   : 李泽雄
# @BoKeYuan : 小家电维修
# @File     : comment_hander.py
# @Version  : Python 3.10.10
# @Project  : python3
# @Software : PyCharm




def add_node(tree_dic,comment):
    if comment.parent_comment is None:
        #如果我是顶层，那我放在这
        tree_dic[comment] ={}
    else:#循环当前整个dict，直到找到为止
        for k,v in tree_dic.items():
            if k == comment.parent_comment: #找到了你爸
                print("find dad.",k)
                tree_dic[comment.parent_comment][comment] = {}
            else: #进入下一层继续找
                print("keep going deeper....")
                add_node(v,comment)

def render_tree_node(tree_dic,margin_val):
    html = ""
    for k,v in tree_dic.items():
        ele = "<div class='comment-node' style='margin-left:%spx'>" % margin_val + k.comment  + "<span style='margin-left:20px'>%s </span>"%k.date + \
                "<span style='margin-left:20px'>%s</span>" %k.user.name \
              +  '<span comment-id="%s"' % k.id +' style="margin-left:20px" class="glyphicon glyphicon-comment add-comment" aria-hidden="true"></span>'\
              +  "</div>"
        html += ele
        html += render_tree_node(v,margin_val+16)
    return html
def render_comment_tree(tree_dic):
    html = ""
    for k,v in tree_dic.items():
        ele = "<div class='root-comment'>" + k.comment + "<span style='margin-left:20px'>%s </span>"%k.date \
              + "<span style='margin-left:20px'>%s</span>" %k.user.name \
              + '<span comment-id="%s"' % k.id +' style="margin-left:20px" class="glyphicon glyphicon-comment add-comment" aria-hidden="true"></span>'\
              +  "</div>"
        html += ele
        html += render_tree_node(v,10)
    return html

def build_tree(comment_set):
    tree_dic = {}
    for comment in comment_set:
        #把存储树的空字典以及所有评论传到专门递归的函数里面去处理
        add_node(tree_dic,comment)

    for k,v in tree_dic.items():
        print (k,v)
    return tree_dic