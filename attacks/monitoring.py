#-*-coding: utf-8-*-
from subprocess import Popen
import time

def monitoring():
    # Cria arquivo usado para os fluxos e arquivo usado para a memória.
    aggregate_flows_file = open('aggregate_flow_file','a')    
    memory_metrics_file = open('memory_metrics_file','a')    
    # Comandos para buscar o fluxo e o uso de memória.
    cmd_flow = "sudo ovs-ofctl dump-aggregate s1"
    cmd_memory = "sar -r 1 1"
    while(True):
        p_flow = Popen(cmd_flow.split(), stdout=aggregate_flows_file)
        p_memory = Popen(cmd_memory.split(), stdout=memory_metrics_file)
        time.sleep(30)

monitoring()