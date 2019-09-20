import os
import sys
import argparse

def get_parser(add_help=False):

    #region arguments yapf: disable
    # parameter priority: command line > config > default
    parser = argparse.ArgumentParser( add_help=add_help, description='IO Processor')
    parser.add_argument('-model', '--model_id', default=None, help='action or face')
    parser.add_argument('-u', '--user_id', default=None, help='user id')
    parser.add_argument('-name', '--picture',default=None, help='picture name')
    parser.add_argument('-method', '--methods', default=None, help='methods name')
    parser.add_argument('-ip1', '--web_camera', default=None, help='picture name')
    parser.add_argument('-ip2', '--rtmpUrl', default=None, help='methods name')
    # processor
    parser.add_argument('--device', type=int, default=0, nargs='+', help='the indexes of GPUs')

    return parser

parser = get_parser(add_help=False)
arg = parser.parse_args()

if (arg.model_id == '0'):
    print('model!')
    start_docker = 'docker start 0d5c01b7a595'
    os.system(start_docker)
    run_docker = "docker exec -it 0d5c01b7a595 /bin/bash -c 'cd /workspace/liu/remote_workspace/catgan_pytorch-master && python dehaze.py {} {}'".format(arg.picture, arg.methods)
    os.system(run_docker)
    # os.system("docker logs -f 0d5c01b7a595")
else :
    if (arg.model_id == '1'):
        print('video model!')
        start_docker = 'docker start 0d5c01b7a595'
        os.system(start_docker)
        run_docker = "docker exec -it 0d5c01b7a595 /bin/bash -c 'cd /workspace/liu/remote_workspace/catgan_pytorch-master && python dehaze1.py {} {}'".format(arg.picture, arg.methods)
        os.system(run_docker)
        # os.system("docker logs -f 0d5c01b7a595")
    else :
        print('invalid_model')









def get_parser(add_help=False):

    #region arguments yapf: disable
    # parameter priority: command line > config > default
    parser = argparse.ArgumentParser( add_help=add_help, description='IO Processor')
    parser.add_argument('-model', '--model_id', default=None, help='action or face')
    parser.add_argument('-u', '--user_id', default=None, help='user id')
    parser.add_argument('-ip1', '--web_camera',default=None, help='ip of web camera')
    parser.add_argument('-ip2', '--rtmpUrl', default=None, help='ip of rtmp')
    # processor
    parser.add_argument('--device', type=int, default=0, nargs='+', help='the indexes of GPUs')

    return parser



