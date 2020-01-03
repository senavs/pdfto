from flask import request
from flask_restplus import Namespace, Resource, fields

import settings
from core.constants import http_code
from core.bo import mypdf
from core.exceptions.mypdf import MyPDFFileError
from core.utils.temb64 import TemporaryBase64
from core.exceptions.temb64 import BrokenBase64

api = Namespace(settings.ENDPOINT_PDFTO, description=settings.ENDPOINT_PDFTO_DESCRIPTION)

NPAGE_INPUT = api.model('npage input', {'file': fields.String(required=True,
                                                              description='File as base64',
                                                              example='TWF0aGV1cyBTZW5hIFZhc2NvbmNlbG9z')})

NPAGE_OUTPUT = api.model('npage output', {'page': fields.Integer(required=True,
                                                                 description='Number of pages in PDF',
                                                                 example=9),
                                          'error': fields.String(required=True,
                                                                 description='If any error occurred',
                                                                 example='File not found or file is not a PDF')})


@api.route(settings.ENDPOINT_PDFTO_ROUTE_NPAGE)
class NPage(Resource):

    @api.response(http_code.SUCCESS_200.code, http_code.SUCCESS_200.description)
    @api.expect(NPAGE_INPUT)
    @api.marshal_with(NPAGE_OUTPUT)
    def post(self):
        input_request = request.json
        output_request = {'page': None, 'error': ''}

        with TemporaryBase64(settings.ENDPOINT_PDFTO_B64_DIRECTORY) as file:
            try:
                file.write_string(input_request['file'])
                output_request['page'] = mypdf.npage(file.file_path)
            except (BrokenBase64, MyPDFFileError) as err:
                output_request['error'] = err.message
                return output_request
        return output_request


TOTEXT_INPUT = api.model('totext input', {'file': fields.String(required=True,
                                                                description='File as base64',
                                                                example='TWF0aGV1cyBTZW5hIFZhc2NvbmNlbG9z')})

TOTEXT_OUTPUT = api.model('totext output', {'text': fields.String(required=True,
                                                                  description='Text extract from PDF',
                                                                  example='This is the text extracted from PDF file'),
                                            'error': fields.String(required=True,
                                                                   description='If any error occurred',
                                                                   example='File not found or file is not a PDF')})


@api.route(settings.ENDPOINT_PDFTO_ROUTE_TOTEXT)
class ToText(Resource):

    @api.response(http_code.SUCCESS_200.code, http_code.SUCCESS_200.description)
    @api.expect(TOTEXT_INPUT)
    @api.marshal_with(TOTEXT_OUTPUT)
    def post(self):
        input_request = request.json
        output_request = {'text': '', 'error': ''}

        with TemporaryBase64(settings.ENDPOINT_PDFTO_B64_DIRECTORY) as file:
            try:
                file.write_string(input_request['file'])
                output_request['text'] = mypdf.totext(file.file_path)
            except (BrokenBase64, MyPDFFileError) as err:
                output_request['error'] = err.message
                return output_request
        return output_request


TOIMAGE_INPUT = api.model('toimage input', {'file': fields.String(required=True,
                                                                  description='File as base64',
                                                                  example='TWF0aGV1cyBTZW5hIFZhc2NvbmNlbG9z')})

TOIMAGE_OUTPUT = api.model('toimage output', {'image': fields.List(cls_or_instance=fields.String(required=True,
                                                                                                 description='Text extract from PDF',
                                                                                                 example='This is the text extracted from PDF file')),
                                              'error': fields.String(required=True,
                                                                     description='If any error occurred',
                                                                     example='File not found or file is not a PDF')})


@api.route(settings.ENDPOINT_PDFTO_ROUTE_TOIMAGE)
class ToImage(Resource):

    @api.response(http_code.SUCCESS_200.code, http_code.SUCCESS_200.description)
    @api.expect(TOIMAGE_INPUT)
    @api.marshal_with(TOIMAGE_OUTPUT)
    def post(self):
        input_request = request.json
        output_request = {'image': [], 'error': ''}

        with TemporaryBase64(settings.ENDPOINT_PDFTO_B64_DIRECTORY) as file:
            try:
                file.write_string(input_request['file'])
                output_request['image'] = mypdf.toimage(file.file_path)
            except (BrokenBase64, MyPDFFileError) as err:
                output_request['error'] = err.message
                return output_request
        return output_request
