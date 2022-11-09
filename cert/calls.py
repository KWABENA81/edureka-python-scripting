from subprocess import run

# sth = subprocess.call('curl', '-X', 'GET', '-d',  # flow-x,
#                       'https://nominatim.openstreetmap.org/details?osmtype=R&osmid=' + ''.join(input) + '&format=json')

# xy = run('curl https://example.com 2>/dev/null | grep iana', shell=True)
oosm_type = ['W', 'N', 'R']
for typ in oosm_type:
    xy2 = run(
        'curl \"https://nominatim.openstreetmap.org/details?osmtype=' + ''.join(
            typ) + '&osmid=175905&format=json\" 2>/dev/null | grep error',
        shell=True)
    if xy2.returncode == 1:
        xy2 = run(
            'curl \"https://nominatim.openstreetmap.org/details?osmtype=' + ''.join(
                typ) + '&osmid=175905&format=json\" 2>/dev/null',shell=True)
        print(xy2)

# xy2_r = run(
#     'curl \"https://nominatim.openstreetmap.org/details?osmtype=R&osmid=175905&format=json\" 2>/dev/null | grep error',
#     shell=True)
# xy2_n = run(
#     'curl \"https://nominatim.openstreetmap.org/details?osmtype=N&osmid=175905&format=json\" 2>/dev/null | grep error',
#     shell=True)
# xy2_w = run(
#     'curl \"https://nominatim.openstreetmap.org/details?osmtype=W&osmid=175905&format=json\" 2>/dev/null | grep error',
#     shell=True)
#


# curl "https://nominatim.openstreetmap.org/details?osmtype=R&osmid=175885&format=json"
