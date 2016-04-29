#!/bin/sh

python pulley.py 3 \
     -ksp_type cg \
     -ksp_monitor_true_residual \
     -pc_type composite \
     -pc_composite_type additive \
     -pc_composite_pcs python,python \
     -sub_0_pc_python_type impl.PatchPC \
     -sub_0_sub_ksp_type preonly \
     -sub_0_sub_pc_type lu \
     -sub_1_pc_python_type impl.P1PC \
     -sub_1_lo_pc_type lu

