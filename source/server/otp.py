from flask import Flask, render_template, request
import pyotp
import qrcode
import base64


def create_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Convert the QR code image to base64
    qr_image_bytes = qr_image.tobytes()
    qr_image_base64 = base64.b64encode(qr_image_bytes)#.decode("utf-8")

    return qr_image_base64

def provision_otp(user_name="newbi"):

    secret_key = pyotp.random_base32()
    provisioning_uri = pyotp.totp.TOTP(secret_key).provisioning_uri(name=user_name, issuer_name='worldcomputer.info')
    qr_endcoded = create_qr_code(provisioning_uri)
     
    return secret_key, provisioning_uri, qr_endcoded


def generate_otp(secret_key):

    return pyotp.totp.TOTP(secret_key).now()

def verify_otp(secret_key, otp):

    return pyotp.totp.TOTP(secret_key).verify(otp)