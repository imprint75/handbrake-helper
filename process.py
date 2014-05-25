import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='handbrake helper')
parser.add_argument('-i', '--input', help='Input file name', required=True)
parser.add_argument('-o', '--output', help='Output file name', required=False)
parser.add_argument('-f', '--format', help='File format', required=True)
args = parser.parse_args()

command = ['HandBrakeCLI', '-i', '-o', '-e', 'x264', '-q', '20.0', '-a',
           '1,1', '-E', 'faac,copy:ac3', '-B', '160,160', '-6',
           'dpl2,none', '-R', 'Auto,Auto', '-D', '0.0,0.0',
           '--audio-copy-mask', 'aac,ac3,dtshd,dts,mp3',
           '--audio-fallback', 'ffac3', '-f', 'mp4', '-4', '--decomb',
           '--loose-anamorphic', '--modulus', '2', '-m', '--x264-preset',
           'medium', '--h264-profile', 'high', '--h264-level', '4.1']


def main():
    if os.path.exists(args.input):
        for f in os.listdir(args.input):
            if f.endswith(args.format):
                i = ''.join([args.input, f])
                o = ''.join([args.input, f.rstrip(args.format), 'mp4'])
                command.insert(command.index('-i') + 1, i)
                command.insert(command.index('-o') + 1, o)
                subprocess.call(command)
    else:
        print '::path doesnt exist'

if __name__ == '__main__':
    main()
