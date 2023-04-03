from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
    s=Serializer('JASHFVNASR8FU32@2R',seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
