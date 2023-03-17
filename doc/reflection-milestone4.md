## Reflection (Milestone 4)

### Implemented Features

* All the input control (Checkbox, Ranger Sliders) are functional and can control the charts
* The two tabs are set up to group the visualisations into two main sections : namely “General Information” and “Sleep Stages”
* All charts are linked to the datasets and can be refreshed instantly upon the change of the input values.
* The application is deployed and published to herokuapp.com.  Note that the link is not acessible to the public due to the charging policy of herouapp. Therefore we will show to the TA our product, as in the previous milestones.
* Basically, all features which were proposed in the design phase have been implemented and completed in milestone 4 successfully.

### Comment Received and Followup
In the whole project, we have received some valuable feedback/comment from the TA and fellow classmates.  Studies, investigation, alternative proposal, and/or implementation have been taken seriously and well communicated to address all these comment, including :
* In the first lab session, a comment from fellow classmate suggested us to add tooltips in our charts.  This suggestion was then implemented, completed and delivered successfully.
* In our first release, all of our charts were all only grouped by (i.e. color-by) Gender. The TA suggested us to add a new user input control option to allow configuring the charts to be grouped by (i.e. color-by) Gender as well as Smoke-Status.  Evaluation was done and we believed this is a good suggestion.  As a result of this design change, we have also consulted the TA and agreed with him to make some minor changes (i.e. removing the existing "Smoke Status checkbox") because this would make the overall control more sensible (as a result of the introduction of the Group-By 'Smoking Status' feature.  We finally implemented his suggestion in our 4th Milestone. 
* The TA also suggested to add title for the x-axis of all our 'count' bar charts.  His suggestion was well taken and titles have been added in the Milestone 4.
* In the early stage, the TA once suggested to add some 'error bars' in our bar charts.  Studies and testing were conducted.  After a no. of testing however, we found that this may not be feasible in our case, because our existing charts were all based on count/frequency and we, later, understood that the altair mark_errorbars() function do not work with the count data.  We believe this result is kind of sensible because the measures of error (or standard deviation/confidence interval) are applied to attributes value, not on the count value.  He also mentioned that other team couldn't make it work either.  Therefore, we finally agreed with the TA to withdraw this suggestion.

### Limitation

* Because of the adoption of iframe, the display of the charts may not be very responsive.  When the app is viewed across different mobile devices with varying screen resolution, the complete charts may not be viewable easily.



