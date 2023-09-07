baseruby="echo executable host ruby is required.  use --with-baseruby option.; false"
_\
=begin
_=
ruby="${RUBY-$baseruby}"
case "$ruby" in "echo "*) $ruby; exit $?;; esac
case "$0" in /*) r=-r"$0";; *) r=-r"./$0";; esac
exec $ruby "$r" "$@"
=end
=baseruby
class Object
  remove_const :CROSS_COMPILING if defined?(CROSS_COMPILING)
  CROSS_COMPILING = RUBY_PLATFORM
  constants.grep(/^RUBY_/) {|n| remove_const n}
  RUBY_VERSION = "3.0.6"
  RUBY_RELEASE_DATE = "2023-03-30"
  RUBY_PLATFORM = "x86_64-linux"
  RUBY_PATCHLEVEL = 216
  RUBY_REVISION = "23a532679b406cb53c0edfc00c91c32a5ccd335a"
  RUBY_COPYRIGHT = "ruby - Copyright (C) 1993-2023 Yukihiro Matsumoto"
  RUBY_ENGINE = "ruby"
  RUBY_ENGINE_VERSION = "3.0.6"
  RUBY_DESCRIPTION = RubyVM.const_defined?(:MJIT) && RubyVM::MJIT.enabled? ?
    "ruby 3.0.6p216 (2023-03-30 revision 23a532679b) +JIT [x86_64-linux]" :
    "ruby 3.0.6p216 (2023-03-30 revision 23a532679b) [x86_64-linux]"
end
builddir = File.dirname(File.expand_path(__FILE__))
srcdir = "."
top_srcdir = File.realpath(srcdir, builddir)
fake = File.join(top_srcdir, "tool/fake.rb")
eval(File.binread(fake), nil, fake)
ropt = "-r#{__FILE__}"
["RUBYOPT"].each do |flag|
  opt = ENV[flag]
  opt = opt ? ([ropt] | opt.b.split(/\s+/)).join(" ") : ropt
  ENV[flag] = opt
end
