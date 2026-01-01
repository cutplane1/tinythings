map(-> $x {
    given $x {
        when .d {print $x.basename ~ "/" ~ " \n";}
        default {print $x.basename ~ " \n";}
    }
}, dir(@*ARGS[0] // "."));
