import misc_tools
import random

# this is taking section_B and the antenna kit and merging into one set of parts

def create_routing(env, first_step='op26'):

    tasks = {
        'op26': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.3,
            'run_time': 2.81,
            'teardown_time': 0.16,
            'route_to': 'op27'
        },
        'op27': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.14,
            'run_time': 1.91,
            'teardown_time': 0,
            'route_to': 'op28'
        },

        'op28': misc_tools.make_quality_step(
            env=env,
            run_time=75,
            route_to=env['section_C_kanban'],
            transit_time=0
            ),

    }

    return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def get_bom(env):
    # note that these quantities are not double checked, so they are 
    # just placeholders for now

    return {
        'section_B': {
            'location': env['section_B_kanban'],
            'qty': 1
        },
        'antenna_kit': {
            'location': env['antenna_kit_storage'],
            'qty': 1
        }
    }

def create_kanban_attrs(env):

    return misc_tools.make_kanban_attrs(order_gen=env['gener.section_C'],
        order_point=0, order_qty=0,
        init_qty=0, warmup_time=0)
    # what are the details of this specific kanban?order point, order quantity, etc.
    # because I just made mine up
    

	