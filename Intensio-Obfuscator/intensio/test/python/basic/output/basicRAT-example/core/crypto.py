# -*- coding: utf-8 -*-
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from common import OwBGcBlzySYfaqOsrGimMtFLwhqqzoHn, GutZpRlAsBCAvPyzhYlxoAGyimkaOLTR
SFagktkTtZekEMGVBphiRtNlhUsbBkQV = 'b14ce95fa4c33ac2803782d18341869f'
class BYVeWyLbFkltjKWrDjegeXKcUssDeTKO(Exception):
    pass
def vWjgdxXYnuWzHdIgfVdzZMtMLXBSYlyO(cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu, kGYTWSfvuDprKpGLiqehVAXxBnCjSGTy=AES.block_size):
    JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr = (kGYTWSfvuDprKpGLiqehVAXxBnCjSGTy - (len(cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu) % kGYTWSfvuDprKpGLiqehVAXxBnCjSGTy))
    return cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu + (chr(JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr)*JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr)
def ZHNWQUoRTObwubduvNbfpXTTgDmTZKvn(cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu):
    JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr = cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu[-1]
    if cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.endswith(JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr*ord(JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr)):
        return cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu[:-ord(JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr)]
    raise BYVeWyLbFkltjKWrDjegeXKcUssDeTKO("PKCS7 improper padding {}".format(repr(cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu[-32:])))
def wkCBVuXegTSBSYDZQBgxxzkMPxVjzQTk(sock, server=True, bits=2048):
    jWOhPeWyYiAMZGeISnknzYlvOIKdtTqh = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF;
    rRQELiHSLLIvcXpENiaDcjkZgdzOIjjF = 2
    IFSUonXzgpHrRBEOMrPKpFLYIQgZprUK = GutZpRlAsBCAvPyzhYlxoAGyimkaOLTR(os.urandom(32))
    OWadEIqCEBYnuuSobZANrHReNXyaDRqc = pow(rRQELiHSLLIvcXpENiaDcjkZgdzOIjjF, IFSUonXzgpHrRBEOMrPKpFLYIQgZprUK, jWOhPeWyYiAMZGeISnknzYlvOIKdtTqh)
    if server:
        sock.send(OwBGcBlzySYfaqOsrGimMtFLwhqqzoHn(OWadEIqCEBYnuuSobZANrHReNXyaDRqc))
        b = GutZpRlAsBCAvPyzhYlxoAGyimkaOLTR(sock.recv(4096))
    else:
        b = GutZpRlAsBCAvPyzhYlxoAGyimkaOLTR(sock.recv(4096))
        sock.send(OwBGcBlzySYfaqOsrGimMtFLwhqqzoHn(OWadEIqCEBYnuuSobZANrHReNXyaDRqc))
    cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu = pow(b, IFSUonXzgpHrRBEOMrPKpFLYIQgZprUK, jWOhPeWyYiAMZGeISnknzYlvOIKdtTqh)
    return SHA256.new(OwBGcBlzySYfaqOsrGimMtFLwhqqzoHn(cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu)).digest()
def LQOdRjWyVheTJCytAXEImYNlfGEClgVr(FBiZhERjRTSYNAHXoxwNtggMpCdWNhHQ, KEY):
    FBiZhERjRTSYNAHXoxwNtggMpCdWNhHQ = vWjgdxXYnuWzHdIgfVdzZMtMLXBSYlyO(FBiZhERjRTSYNAHXoxwNtggMpCdWNhHQ)
    suTxuEfWzfiCIFuyEIMwDiqpalSGJeUY = Random.new().read(AES.block_size)
    hTctnvcTpOxmBvYoRVfIsTKzevglmhJw = AES.new(KEY, AES.MODE_CBC, suTxuEfWzfiCIFuyEIMwDiqpalSGJeUY)
    return suTxuEfWzfiCIFuyEIMwDiqpalSGJeUY + hTctnvcTpOxmBvYoRVfIsTKzevglmhJw.encrypt(FBiZhERjRTSYNAHXoxwNtggMpCdWNhHQ)
def xYJEIEJwYxrIrxmzUDOdGnbQaPoRNnfl(ciphertext, KEY):
    suTxuEfWzfiCIFuyEIMwDiqpalSGJeUY = ciphertext[:AES.block_size]
    hTctnvcTpOxmBvYoRVfIsTKzevglmhJw = AES.new(KEY, AES.MODE_CBC, suTxuEfWzfiCIFuyEIMwDiqpalSGJeUY)
    FBiZhERjRTSYNAHXoxwNtggMpCdWNhHQ = hTctnvcTpOxmBvYoRVfIsTKzevglmhJw.decrypt(ciphertext[AES.block_size:])
    return ZHNWQUoRTObwubduvNbfpXTTgDmTZKvn(FBiZhERjRTSYNAHXoxwNtggMpCdWNhHQ)
