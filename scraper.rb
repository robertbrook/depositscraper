require 'rubygems'
require 'hpricot'
require 'open-uri'
require 'enumerator'

doc = Hpricot.XML(open("http://deposits.parliament.uk/"))
targets = Array.new

(doc/"tr/td[@bgcolor='#e3e3e3']").each do |td|
  targets << td.inner_html
end
   
targets.slice!(0..4)
targets.each_slice(5) {|a| p a}
