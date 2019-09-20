import os
import sys
import argparse

def get_parser(add_help=False):

    #region arguments yapf: disable
    # parameter priority: command line > config > default
    parser = argparse.ArgumentParser( add_help=add_help, description='IO Processor')
    parser.add_argument('-model', '--model_id', default=None, help='action or face')
    parser.add_argument('-u', '--user_id', default=None, help='user id')
    parser.add_argument('-uuid', '--uuid', default=None, help='id for identification')
    parser.add_argument('--image','--image',default=None,help='Path to image')
    parser.add_argument('-result', '--result', default=None, help='Path to result')

    # processor
    parser.add_argument('--device', default=0, nargs='+', help='the indexes of GPUs')

    return parser

parser = get_parser(add_help=False)
arg = parser.parse_args()

if (arg.model_id == '0'):
    print('jiechuwang!')
    start_docker = 'docker restart e2baf410410e'
    os.system(start_docker)
    run_docker = "docker exec -it e2baf410410e /bin/bash -c 'cd /teds/object_detection/vocteds_flaw/ && python main.py  --video {} --result {} -uid {} -u {} '".format(arg.image, arg.result, arg.uuid, arg.user_id)
    os.system(run_docker)
    # os.system("docker logs --tail 0 -f st-gcn3")
    print("end")
else :
    if (arg.model_id == '1'):
        print('face_recognition!')
        start_docker = 'docker start 0d5c01b7a595'
        os.system(start_docker)
        run_docker = "docker exec -it 0d5c01b7a595 /bin/bash -c 'cd /workspace/liu/remote_workspace/help_note/python/server && python Camera.py {} {}'".format(arg.web_camera, arg.rtmpUrl)
        os.system(run_docker)
        os.system("docker logs -f 0d5c01b7a595")
    else :
        print('invalid_model')









def get_parser(add_help=False):

    #region arguments yapf: disable
    # parameter priority: command line > config > default
    parser = argparse.ArgumentParser( add_help=add_help, description='IO Processor')
    parser.add_argument('-model', '--model_id', default=None, help='action or face')
    parser.add_argument('-u', '--user_id', default=None, help='user id')
    parser.add_argument('-uid', '--uid', default=None, help='id for identification')
    parser.add_argument('--video',default='./resource/media/skateboarding.mp4',help='Path to video')
    # processor
    parser.add_argument('--device', type=int, default=0, nargs='+', help='the indexes of GPUs')

    return parser