import misc_tools
import random

# this is taking multiplexer and OPTX and merging them into one group of items

def create_routing(env, first_step='move21'):

    tasks = {
        'move21': {
            'location': env['multiplexer_kanban'],
            # is this the right location to have the move take place from?
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 1,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op21'
        },
        'op21': {
            'location': env['assembly_bench'],
            # make sure that this assembly bench is the same place that the next move picks up from!!
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.07,
            'run_time': 1.38,
            'teardown_time': 0.05,
            'route_to': 'move22'
        },
        'move22': {
            'location': env['assembly_bench'],
            # link to location from op21
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 1,
            'teardown_time': 0,
            'transit_time': 0,
            'route_to': 'op22'
        },
        'op22': {
            'location': env['assembly_bench'],
            'worker': env['assembler'],
            'manned': True,
            'setup_time': 0.14,
            'run_time': 1.91,
            'teardown_time': 0,
            'route_to': env['section_A_kanban']
        },

    }

    return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def get_bom(env):
    # note that these quantities are not double checked, so they are 
    # just placeholders for now

    return {
        'optx': {
            'location': env['optx_kanban'],
            'qty': 1
        },
        'multiplexer': {
            'location': env['multiplexer_kanban'],
            'qty': 1
        }
    }

def create_kanban_attrs(env):

    return misc_tools.make_kanban_attrs(order_gen=env['gener.section_A'],
        order_point=0, order_qty=0,
        init_qty=0, warmup_time=0)
    # what are the details of this specific kanban?order point, order quantity, etc.
    # because I just made mine up
    

	