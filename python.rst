Test and profiling:
===================

One can simply begin by using ``nosetests --with-timer`` that displays detail for each test run.

However this may hide long setup/teardown times in a test case. The you may want to do some more profiling



Graphical output:
-----------------


    Using cprofile with nose an visualization tool:
        pip install nose-cprof
        pip install gprof2dot

    then try:

        nosetests --with-cprofile

    This generates a stats.dat file one can reuse using (feh is a simple image viewer):

        gprof2dot -f pstats stats.dat | dot -Tpng -o output.png ; feh output.png


    Sources :
        https://github.com/mahmoudimus/nose-timer/
        https://github.com/jrfonseca/gprof2dot
        http://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script

    See also :
        https://github.com/jrfonseca/xdot.py
        https://julien.danjou.info/blog/2015/guide-to-python-profiling-cprofile-concrete-case-carbonara
        http://stefaanlippens.net/python_profiling_with_pstats_interactive_mode/


(further readings:
    http://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution)
    http://darcs.idyll.org/~t/projects/pinocchio/doc/#figleafsections-find-out-what-tests-are-executing-which-parts-of-your-code
    https://ymichael.com/2014/03/08/profiling-python-with-cprofile.html
    http://stackoverflow.com/questions/3898266/what-is-this-cprofile-result-telling-me-i-need-to-fix
    http://stackoverflow.com/questions/12236474/how-to-use-cprofile-with-nosetest-with-profile

