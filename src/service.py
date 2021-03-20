from flask_restful import Resource, reqparse, request
import time
from utils import KEY_DATA, H_LANG, EN_US, ZH_CN, DE_DE, PR_PR, HEADER_TAG
from db import Lang as lang

class Lang(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(H_LANG, type=str, location=HEADER_TAG, required=True)
 
    def get(self, pageId):
        data = self.reqparse.parse_args()
        data[H_LANG] = request.headers[H_LANG]

        if data[H_LANG] == EN_US:
            return {KEY_DATA: lang.EN[pageId] }, 200
        
        if data[H_LANG] == ZH_CN:
            return {KEY_DATA: lang.CH[pageId] }, 200

        if data[H_LANG] == DE_DE:
            return {KEY_DATA: lang.DE[pageId] }, 200
        
        #if data[H_LANG] == ES_ES:
         #   return {KEY_DATA: lang.ES[pageId] }, 200
        
        if data[H_LANG] == PR_PR:
            return {KEY_DATA: lang.PR[pageId] }, 200
       
        return {KEY_DATA: lang.EN[pageId] }, 200