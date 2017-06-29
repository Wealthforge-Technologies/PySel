=============
== INSTALL ==
=============

Using python 3.6

Using selenium jar
$ java -jar selenium-server-standalone-3.4.0.jar -port 4445
- note that this port can be changed



============
== TRICKS ==
============

- Scrolling to an element:

self.driver.execute_script("arguments[0].scrollIntoView();", elem)
OR
elem.send_keys(Keys.NULL)

NOTE: I'm not sure which is better!!!!