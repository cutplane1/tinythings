map(-> $x {
    given $x {
        when .d {print $x.basename ~ "/" ~ " ";}
        default {print $x.basename ~ " ";}
    }
}, dir(@*ARGS[0] // "."));
