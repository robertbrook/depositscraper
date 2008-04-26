require 'rubygems'
require 'hpricot'
require 'open-uri'

doc = Hpricot.XML(open("http://deposits.parliament.uk/"))

(doc/"tr").each do |tr|
  
  (tr/"td[@bgcolor='#e3e3e3'").each do |td|
    p td.inner_html
  end
   
end