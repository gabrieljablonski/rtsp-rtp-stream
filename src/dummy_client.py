import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))

sleep(10)
rtp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rtp.bind(('localhost', 8000))
rtp.settimeout(0.1)

setup = '\r\n'.join((
    'SETUP rtsp://movie.mjpeg RTSP/1.0',
    'CSeq: 3',
    'Transport: RTP/AVP;unicast;client_port=8000-8001',
)) + '\r\n'
s.send(setup.encode())
print(s.recv(4096))
play = '\r\n'.join((
    'PLAY rtsp://movie.mjpeg RTSP/1.0',
    'CSeq: 4',
    'Range: npt=5-20',
    'Session: 12345678',
)) + '\r\n'
s.send(play.encode())
print(s.recv(4096))
sleep(1)
pause = '\r\n'.join((
    'PAUSE rtsp://movie.mjpeg RTSP/1.0',
    'CSeq: 5',
    'Session: 12345678',
)) + '\r\n'
s.send(pause.encode())
print(s.recv(4096))
sleep(1)
play = '\r\n'.join((
    'PLAY rtsp://movie.mjpeg RTSP/1.0',
    'CSeq: 6',
    'Session: 12345678',
)) + '\r\n'
s.send(play.encode())
print(s.recv(4096))
sleep(1)
teardown = '\r\n'.join((
    'TEARDOWN rtsp://movie.mjpeg RTSP/1.0',
    'CSeq: 7',
    'Session: 12345678',
)) + '\r\n'
s.send(teardown.encode())
print(s.recv(4096))
sleep(1)
s.close()
