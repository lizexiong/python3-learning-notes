#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from Arya.backends.base_module import BaseSaltModule


class File(BaseSaltModule):

    pass
    def is_required(self,*args,**kwargs):
        file_path = args[1]
        cmd = "test -f %s;echo $?" % file_path
        return cmd