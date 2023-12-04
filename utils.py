from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('55686D6B6A6679566A42376943524637554F755775754366665A307449586C6C3351644A6741635349524D3D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code} کد تایید شما '
        }
        api.sms_send(params)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

