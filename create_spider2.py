import argparse
from solid. utilsimport *


def create_spider(args):
    w_body = args.get('w_body')
    l_body = args.get('l_body')
    h_body = args.get('h_body')

    leg_length = args.get('leg_length')
    cube_main = color(BlackPaint)(cube([w_body, l_body, h_body], center=True))
    s_of = l_body/2 + h_body/2
    sphere_back = back(s_of)(color(BlackPaint)(sphere(r=h_body/2)))

    leg_p1_so = w_body/2 + leg_length/8
    leg_p2_so = w_body/2 + leg_length/8 + leg_length/4
    leg_p3_so = w_body/2 + leg_length/8 + leg_length/4 + leg_length/6

    leg_p1_d = h_body/2 - 1/2
    leg_p2_d = h_body/2 - 2
    leg_p3_d = h_body/2 + leg_length/16

    leg14_fb = l_body/2 - 1/2
    leg23_fb = l_body/2 - l_body/3

    leg1_cyl = cylinder(r=1, h=leg_length/4, center=True)
    leg_p1 = rotate(a=120, v=(1, -1, -1))(color(BlackPaint)(leg1_cyl))
    leg2_cyl = cylinder(r=1, h=leg_length/3, center=True)
    leg_p2 = rotate(a=120, v=(0, -1, 0))(color(BlackPaint)(leg2_cyl))
    leg3_cyl = cylinder(r=1, h=leg_length*5/12, center=True)
    leg_p3 = rotate(a=0, v=(-1, -1, 1))(color(BlackPaint)(leg3_cyl))
    leg1_cyl = cylinder(r=1, h=leg_length/4, center=True)
    leg_p1 = rotate(a=120, v=(1, -1, -1))(color(BlackPaint)(leg1_cyl))
    leg2_cyl = cylinder(r=1, h=leg_length/3, center=True)
    leg_p2 = rotate(a=120, v=(0, -1, 0))(color(BlackPaint)(leg2_cyl))
    leg3_cyl = cylinder(r=1, h=leg_length*5/12, center=True)
    leg_p3 = rotate(a=0, v=(-1, -1, 1))(color(BlackPaint)(leg3_cyl))
    leg_p2l = rotate(a=120, v=(0, 1, 0))(color(BlackPaint)(leg2_cyl))

    rleg1_p1 = forward(leg14_fb)(right(leg_p1_so)(down(leg_p1_d)(leg_p1)))
    rleg1_p2 = forward(leg14_fb)(right(leg_p2_so)(down(leg_p2_d)(leg_p2)))
    rleg1_p3 = forward(leg14_fb)(right(leg_p3_so)(down(leg_p3_d)(leg_p3)))
    rleg1 = rleg1_p1 + rleg1_p2 + rleg1_p3

    rleg2_p1 = forward(leg23_fb)(right(leg_p1_so)(down(leg_p1_d)(leg_p1)))
    rleg2_p2 = forward(leg23_fb)(right(leg_p2_so)(down(leg_p2_d)(leg_p2)))
    rleg2_p3 = forward(leg23_fb)(right(leg_p3_so)(down(leg_p3_d)(leg_p3)))
    rleg2 = rleg2_p1 + rleg2_p2 + rleg2_p3

    rleg3_p1 = back(leg23_fb)(right(leg_p1_so)(down(leg_p1_d)(leg_p1)))
    rleg3_p2 = back(leg23_fb)(right(leg_p2_so)(down(leg_p2_d)(leg_p2)))
    rleg3_p3 = back(leg23_fb)(right(leg_p3_so)(down(leg_p3_d)(leg_p3)))
    rleg3 = rleg3_p1 + rleg3_p2 + rleg3_p3

    rleg4_p1 = back(leg14_fb)(right(leg_p1_so)(down(leg_p1_d)(leg_p1)))
    rleg4_p2 = back(leg14_fb)(right(leg_p2_so)(down(leg_p2_d)(leg_p2)))
    rleg4_p3 = back(leg14_fb)(right(leg_p3_so)(down(leg_p3_d)(leg_p3)))
    rleg4 = rleg4_p1 + rleg4_p2 + rleg4_p3

    lleg1_p1 = forward(leg14_fb)(left(leg_p1_so)(down(leg_p1_d)(leg_p1)))
    lleg1_p2 = forward(leg14_fb)(left(leg_p2_so)(down(leg_p2_d)(leg_p2l)))
    lleg1_p3 = forward(leg14_fb)(left(leg_p3_so)(down(leg_p3_d)(leg_p3)))
    lleg1 = lleg1_p1 + lleg1_p2 + lleg1_p3

    lleg2_p1 = forward(leg23_fb)(left(leg_p1_so)(down(leg_p1_d)(leg_p1)))
    lleg2_p2 = forward(leg23_fb)(left(leg_p2_so)(down(leg_p2_d)(leg_p2l)))
    lleg2_p3 = forward(leg23_fb)(left(leg_p3_so)(down(leg_p3_d)(leg_p3)))
    lleg2 = lleg2_p1 + lleg2_p2 + lleg2_p3

    lleg3_p1 = back(leg23_fb)(left(leg_p1_so)(down(leg_p1_d)(leg_p1)))
    lleg3_p2 = back(leg23_fb)(left(leg_p2_so)(down(leg_p2_d)(leg_p2l)))
    lleg3_p3 = back(leg23_fb)(left(leg_p3_so)(down(leg_p3_d)(leg_p3)))
    lleg3 = lleg3_p1 + lleg3_p2 + lleg3_p3

    lleg4_p1 = back(leg14_fb)(left(leg_p1_so)(down(leg_p1_d)(leg_p1)))
    lleg4_p2 = back(leg14_fb)(left(leg_p2_so)(down(leg_p2_d)(leg_p2l)))
    lleg4_p3 = back(leg14_fb)(left(leg_p3_so)(down(leg_p3_d)(leg_p3)))
    lleg4 = lleg4_p1 + lleg4_p2 + lleg4_p3

    left_legs = lleg1 + lleg2 + lleg3 + lleg4
    right_legs = rleg1 + rleg2 + rleg3 + rleg4

    spider = cube_main + sphere_back + left_legs + right_legs
    scad_render_to_file(spider, './file_out.scad')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Please specify \
        body measurements and leg length')
    parser.add_argument(
        'w_body', metavar='w_body', type=int, nargs='?', default=10,
        help='body height')
    parser.add_argument(
        'h_body', metavar='h_body', type=int, nargs='?', default=7,
        help='body width')
    parser.add_argument(
        'l_body', metavar='l_body', type=int, nargs='?', default=20,
        help='body length')
    parser.add_argument(
        'leg_length', metavar='leg_length', type=int, nargs='?',
        default=20, help='leg length')
    args = parser.parse_args()

    create_spider(vars(args))
