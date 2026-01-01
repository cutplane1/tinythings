my @all_files = dir(".");
my @cur_files = @all_files.map({if $_.basename ~~ "uuuu.raku" or $_.basename.ends-with("final.zip") {} else { $_ } }).grep({ defined $_ });
my $zip_file_with_longest_name = @all_files.grep({ $_.basename.ends-with(".zip") }).max({ $_.basename.chars });
if $zip_file_with_longest_name.WHAT ~~ Num {
    $zip_file_with_longest_name = ~$*CWD.basename ~ ".zip";
} else {
    $zip_file_with_longest_name = ~$zip_file_with_longest_name;
}
shell "7z a " ~ $zip_file_with_longest_name.substr(0, *-4) ~ "-final.zip" ~ " " ~ @cur_files.join(" ");