# izprocess
For processing IZ reports from the joint data sync process. Accepts a CSV as an input with columns including "Network Id", "Existing 035a", "Incoming 035a", and "Action". Outputs a list of records requiring updates and a file for import to Alma if a record meets one of the two following criteria:<br />
<br />
&bull;If a record has the action "match" and the incoming 035a does <i>not</i> match the existing 035a<br />
OR<br />
&bull;If a record has the action "create" and the existing 035a is empty (indicating that the record is new)<br />
<br />
<i>Note: though the column in the report is labelled Network Id, the data included will be Carleton's IZ MMS IDs.</i>
