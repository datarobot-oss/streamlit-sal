# SAL - Style and Layout for Streamlit

## Exhaustive list of SAL placeholders

```sass
%sal-write {}           // Targets the markdown element
%sal-write-container {} // Targets the element-container around the markdown

/*** Text elements ***/
%sal-title {}                     // Targets the h1 element
%sal-title-container {}           // Targets the element-container around the markdown
%sal-title-markdown-container {}  // Targets the markdown element
%sal-title-link-icon {}           // Targets the copy link icon element

%sal-header {}                      // Targets the h2 element
%sal-header-container {}            // Targets the element-container around the markdown
%sal-header-markdown-container {}   // Targets the markdown element
%sal-header-link-icon {}            // Targets the copy link icon element

%sal-subheader {}                     // Targets the h3 element
%sal-subheader-container {}           // Targets the element-container around the markdown
%sal-subheader-markdown-container {}  // Targets the markdown element
%sal-subheader-link-icon {}           // Targets the copy link icon element

%sal-markdown {}           // Targets the markdown element
%sal-markdown-container {} // Targets the element-container around the markdown

/*** Formatted text elements ***/
%sal-caption {}           // Targets the stCaptionContainer element (contains a p tag)
%sal-caption-container {} // Targets the element-container around the caption

%sal-code {}              // Targets the code block element
%sal-code-container {}    // Targets the element-container around the code block
%sal-code-copy-button {}  // Targets the copy content button

%sal-divider {}           // Targets the hr element
%sal-divider-container {} // Targets the element-container around the hr

// %sal-echo will not be supported. Please use st.text+st.write and st.code to style

%sal-latex {}           // Targets the math div element
%sal-latex-container {} // Targets the element-container around the math div

%sal-text {}           // Targets the stText div element (There is no p tag!)
%sal-text-container {} // Targets the element-container around the text

/*** Data elements ***/
%sal-dataframe {}                 // Targets the glideDataEditor div element
%sal-dataframe-container {}       // Targets the element-container around the glideDataEditor div
%sal-dataframe-toolbar {}         // Targets the dataframe toolbar
%sal-dataframe-toolbar-button {}  // Targets the buttons within the dataframe toolbar

%sal-data-editor {}                 // Targets the glideDataEditor div element
%sal-data-editor-container {}       // Targets the element-container around the glideDataEditor div
%sal-data-editor-toolbar {}         // Targets the data-editor toolbar
%sal-data-editor-toolbar-button {}  // Targets the buttons within the data-editor toolbar

// %sal-column-config will not be supported.

%sal-table {}                     // Targets the stTable div element
%sal-table-container {}           // Targets the element-container around the stTable div
%sal-table-fullscreen-button {}   // Targets the fullscreen button of the table

%sal-metric {}       // Targets the element-container around the metric element
%sal-metric-value {} // Targets the stMetricValue div
%sal-metric-delta {} // Targets the stMetricDelta div
%sal-metric-label {} // Targets the label above the metric value

%sal-json {}           // Targets the react-json-view div element
%sal-json-container {} // Targets the element-container around the react-json-view div

/*** Chart elements ***/
// Many Streamlit charts are variations of the stArrowVegaLiteChart
%sal-area-chart {}                    // Targets the stArrowVegaLiteChart div
%sal-area-chart-container {}          // Targets the element-container around the stArrowVegaLiteChart div
%sal-area-chart-fullscreen-button {}  // Targets the fullscreen button of the chart

%sal-line-chart {}                    // Targets the stArrowVegaLiteChart div
%sal-line-chart-container {}          // Targets the element-container around the stArrowVegaLiteChart div
%sal-line-chart-fullscreen-button {}  // Targets the fullscreen button of the chart

%sal-scatter-chart {}                    // Targets the stArrowVegaLiteChart div
%sal-scatter-chart-container {}          // Targets the element-container around the stArrowVegaLiteChart div
%sal-scatter-chart-fullscreen-button {}  // Targets the fullscreen button of the chart

%sal-altair-chart {}                    // Targets the stArrowVegaLiteChart div
%sal-altair-chart-container {}          // Targets the element-container around the stArrowVegaLiteChart div
%sal-altair-chart-fullscreen-button {}  // Targets the fullscreen button of the chart

%sal-vega-lite-chart {}                    // Targets the stArrowVegaLiteChart div
%sal-vega-lite-chart-container {}          // Targets the element-container around the stArrowVegaLiteChart div
%sal-vega-lite-chart-fullscreen-button {}  // Targets the fullscreen button of the chart

%sal-map {}                    // Targets the stDeckGlJsonChart div
%sal-map-container {}          // Targets the element-container around the stDeckGlJsonChart div
%sal-map-fullscreen-button {}  // Targets the fullscreen button of the map

%sal-pydeck-chart {}                    // Targets the stDeckGlJsonChart div
%sal-pydeck-chart-container {}          // Targets the element-container around the stDeckGlJsonChart div
%sal-pydeck-chart-fullscreen-button {}  // Targets the fullscreen button of the pydeck chart

%sal-bokeh-chart {}                    // Targets the stBokehChart div
%sal-bokeh-chart-container {}          // Targets the element-container around the stBokehChart div
%sal-bokeh-chart-fullscreen-button {}  // Targets the fullscreen button of the bokeh chart

%sal-graphviz-chart {}                    // Targets the stGraphVizChart div
%sal-graphviz-chart-container {}          // Targets the element-container around the stGraphVizChart div
%sal-graphviz-chart-fullscreen-button {}  // Targets the fullscreen button of the graphviz chart

%sal-plotly-chart {}                    // Targets the stPlotlyChart div
%sal-plotly-chart-container {}          // Targets the element-container around the stPlotlyChart div
%sal-plotly-chart-fullscreen-button {}  // Targets the fullscreen button of the plotly chart

%sal-pyplot {}                    // Targets the stImage div
%sal-pyplot-container {}          // Targets the element-container around the stImage div
%sal-pyplot-fullscreen-button {}  // Targets the fullscreen button of the pyplot element

/*** Input elements ***/
%sal-button {}              // Targets the button element
%sal-button-container {}    // Targets the element-container around the button

%sal-download-button {}              // Targets the button element
%sal-download-button-container {}    // Targets the element-container around the button

%sal-form-submit-button {}              // Targets the button element
%sal-form-submit-button-container {}    // Targets the element-container around the button

%sal-link-button {}             // Targets the a element
%sal-link-button-container {}   // Targets the element-container around the a tag
%sal-link-button-text {}        // Targets the markdown container within the a tag (contains a p tag)

%sal-page-link {}             // Targets the a element
%sal-page-link-container {}   // Targets the element-container around the a tag
%sal-page-link-text {}        // Targets the markdown container within the a tag (contains a p tag)

%sal-checkbox {}              // Targets the stCheckbox div element
%sal-checkbox-container {}    // Targets the element-container around the stCheckbox div
%sal-checkbox-widget-label {} // Targets the stWidgetLabel div within the stCheckbox div
%sal-checkbox-box {}          // Targets the clickable box
%sal-checkbox-label {}        // Targets the label of the clickable box

%sal-color-picker {}              // Targets the stColorPicker div element
%sal-color-picker-container {}    // Targets the element-container around the stColorPicker div
%sal-color-picker-color-block {}  // Targets the clickable color block where selected color is shown
%sal-color-picker-label {}        // Targets the label of the color picker

%sal-multiselect {}              // Targets the stMultiSelect div element
%sal-multiselect-container {}    // Targets the element-container around the stMultiSelect div
%sal-multiselect-input {}        // Targets the select input div within stMultiSelect div
%sal-multiselect-label {}        // Targets the label of the multiselect

%sal-radio {}               // Targets the stRadio div element
%sal-radio-container {}     // Targets the element-container around the stRadio div
%sal-radio-widget-label {}  // Targets the outside label of the radio element
%sal-radio-group {}         // Targets the group div that holds all selectable items
%sal-radio-item-label {}    // Targets the radio items, contains the radio input and text
%sal-radio-item-markdown {} // Targets all radio item markdown elements (main text)
%sal-radio-item-caption {}  // Targets all radio item caption elements (descriptive text)

%sal-selectbox {}              // Targets the stSelectbox div element
%sal-selectbox-container {}    // Targets the element-container around the stSelectbox div
%sal-selectbox-widget-label {} // Targets the stWidgetLabel div above the stSelectbox div

%sal-select-slider {}              // Targets the stSlider div element
%sal-select-slider-container {}    // Targets the element-container around the stSlider div
%sal-select-slider-widget-label {} // Targets the stWidgetLabel div above the stSlider div
%sal-select-slider-slider {}       // Targets the slider line
%sal-select-slider-selection {}    // Targets the selection bar below the line

%sal-toggle {}              // Targets the stCheckbox div element (st.toggle is named same as st.checkbox!)
%sal-toggle-container {}    // Targets the element-container around the stCheckbox div
%sal-toggle-widget-label {} // Targets the stWidgetLabel div within the stCheckbox div
%sal-toggle-box {}          // Targets the clickable box
%sal-toggle-label {}        // Targets the label of the clickable box

%sal-number-input {}              // Targets the stNumberInput div element
%sal-number-input-container {}    // Targets the element-container around the stNumberInput div
%sal-number-input-widget-label {} // Targets the stWidgetLabel div above the stNumberInput div
%sal-number-input-input {}        // Targets the number input tag

%sal-slider {}              // Targets the stSlider div element (st.slider is named same as st.select_slider!)
%sal-slider-container {}    // Targets the element-container around the stSlider div
%sal-slider-widget-label {} // Targets the stWidgetLabel div above the stSlider div
%sal-slider-slider {}       // Targets the slider line
%sal-slider-selection {}    // Targets the selection bar below the line

%sal-date-input {}              // Targets the stDateInput div element
%sal-date-input-container {}    // Targets the element-container around the stDateInput div
%sal-date-input-widget-label {} // Targets the stWidgetLabel div above the stDateInput div
%sal-date-input-input {}        // Targets the date input tag

%sal-time-input {}              // Targets the stTimeInput div element
%sal-time-input-container {}    // Targets the element-container around the stTimeInput div
%sal-time-input-widget-label {} // Targets the stWidgetLabel div above the stTimeInput div
%sal-time-input-selection {}    // Targets the selection div (not an input!)
%sal-time-input-chevron {}      // Targets the chevron next to the selection div

%sal-date-input {}              // Targets the stDateInput div element
%sal-date-input-container {}    // Targets the element-container around the stDateInput div
%sal-date-input-widget-label {} // Targets the stWidgetLabel div above the stDateInput div
%sal-date-input-input {}        // Targets the date input tag

%sal-text-area {}              // Targets the stTextArea div element
%sal-text-area-container {}    // Targets the element-container around the stTextArea div
%sal-text-area-widget-label {} // Targets the stWidgetLabel div above the stTextArea div
%sal-text-area-instructions {} // Targets the InputInstructions div

%sal-text-input {}              // Targets the input element
%sal-text-input-container {}    // Targets the element-container around the input element
%sal-text-input-widget-label {} // Targets the stWidgetLabel div above the stTextArea div
%sal-text-input-instructions {} // Targets the InputInstructions div

%sal-camera-input {}              // Targets the stWebcamComponent div element
%sal-camera-input-container {}    // Targets the element-container around the stWebcamComponent div
%sal-camera-input-widget-label {} // Targets the stWidgetLabel div above the stTextArea div
%sal-camera-input-video {}        // Targets the video element

%sal-file-uploader {}              // Targets the stFileUploader div element
%sal-file-uploader-container {}    // Targets the element-container around the stFileUploader div
%sal-file-uploader-widget-label {} // Targets the stWidgetLabel div above the stFileUploader div
%sal-file-uploader-drop {}         // Targets the whole drop section element (section tag)
%sal-file-uploader-icon {}         // Targets the drop icon (svg tag)
%sal-file-uploader-text {}         // Targets the instruction text (span tag)
%sal-file-uploader-info {}         // Targets the additional description text (small tag)

/*** Media elements ***/
%sal-audio {}             // Targets the stAudio div element
%sal-audio-container {}   // Targets the element-container around the stAudio div element

%sal-image {}             // Targets the stImage div element
%sal-image-container {}   // Targets the element-container around the stImage div element
%sal-image-image {}       // Targets the image tag
%sal-image-fullscreen-button {}  // Targets the fullscreen button of the stImage div

%sal-video {}             // Targets the stVideo div element
%sal-video-container {}   // Targets the element-container around the stVideo div element

/*** Layout and container elements ***/
%sal-columns {}                 // Targets the a root div element similar to element-container
%sal-columns-column {}          // Targets all column divs within the columns component
%sal-columns-column-content {}  // Targets the vertical content blocks within all child column divs

// This placeholder is special as it does not exist in Streamlit directly
// Use it to wrap col elements returned by `colX, colY = st.columns(n)`
%sal-column {}    // Targets the vertical content block for this specific column

%sal-container {}           // Targets the vertical content block
%sal-container-container {} // Targets the root div around the vertical block 

%sal-container {}           // Targets the vertical content block
%sal-container-container {} // Targets the root div around the vertical block 


%sal-expander {}              // Targets the stExpander div root element
%sal-expander-summary-text {} // Targets the summary text element (span tag)
%sal-expander-chevron {}      // Targets the chevron (svg tag)
%sal-expander-content {}      // Targets the content div stExpanderDetails

%sal-form {}           // Targets the vertical content block
%sal-form-container {} // Targets the root stForm div around the vertical block 

%sal-popover {}           // Targets the button element
%sal-popover-container {} // Targets the root stPopover div around the button

// This placeholder is special as it does not exist in Streamlit directly
// Use it with the popover container returned by `popover = st.popover("Open")`
//  with sal.popover_content('text-bold', container=popover):
//    popover.markdown("Hello World")
%sal-popover-content {}   // Targets the next sibling div which could be any type of component

%sal-sidebar {}           // Targets the stSidebarContent div within the sidebar section
%sal-sidebar-header {}    // Targets the stSidebarHeader div within stSidebarContent div
%sal-sidebar-content {}   // Targets the stSidebarUserContent div within stSidebarContent div

%sal-tabs {}              // Targets the root stTabs div around the component
%sal-tabs-list {}         // Targets the list of available tabs
%sal-tabs-list-buttons {} // Targets the button elements with the tab list
%sal-tabs-panel {}        // Targets the content panel div

// %sal-logo has Alternate support as it lies outside the main container.
// It can be styled directly using %%sal-logo within main.scss but does not allow custom classes

/*** Chat elements ***/
%sal-chat-input {}            // Targets the stChatInput div child element
%sal-chat-input-container {}  // Targets the element-container around the stChatInput div element
%sal-chat-input-text {}       // Targets the textarea element within stChatInput (stChatInputTextArea)
%sal-chat-input-button {}     // Targets the button element within stChatInput (stChatInputSubmitButton)

%sal-chat-message {}           // Targets the stChatMessage root div element
%sal-chat-message-avatar {}    // Targets the avatar div of the message sender (contains an svg)
%sal-chat-message-content {}   // Targets the stChatMessageContent div within the stChatMessage div

/*** Status elements ***/
%sal-success {}             // Targets the stNotification div element
%sal-success-container {}   // Targets the element-container around the stNotification div element
%sal-success-icon {}        // Targets the icon span stAlertDynamicIcon within stNotification div
%sal-success-text {}        // Targets the markdown container within stNotification div (contains a p tag)

%sal-info {}             // Targets the stNotification div element
%sal-info-container {}   // Targets the element-container around the stNotification div element
%sal-info-icon {}        // Targets the icon span stAlertDynamicIcon within stNotification div
%sal-info-text {}        // Targets the markdown container within stNotification div (contains a p tag)

%sal-warning {}             // Targets the stNotification div element
%sal-warning-container {}   // Targets the element-container around the stNotification div element
%sal-warning-icon {}        // Targets the icon span stAlertDynamicIcon within stNotification div
%sal-warning-text {}        // Targets the markdown container within stNotification div (contains a p tag)

%sal-error {}             // Targets the stNotification div element
%sal-error-container {}   // Targets the element-container around the stNotification div element
%sal-error-icon {}        // Targets the icon span stAlertDynamicIcon within stNotification div
%sal-error-text {}        // Targets the markdown container within stNotification div (contains a p tag)

%sal-exception {}            // Targets the stNotification div element
%sal-exception-container {}  // Targets the element-container around the stNotification div element
%sal-exception-message {}    // Targets the div message within stNotification div (contains the text, but no p tag)

%sal-progress {}            // Targets the stProgress div element
%sal-progress-container {}  // Targets the element-container around the stProgress div element
%sal-progress-text {}       // Targets the  markdown container within stProgress div (contains a p tag)
%sal-progress-bar {}        // Targets the progress-bar div within stProgress div

%sal-spinner {}            // Targets the stSpinner child div element
%sal-spinner-container {}  // Targets the element-container around the stSpinner div element
%sal-spinner-text {}       // Targets the  markdown container within stSpinner div (contains a p tag)
%sal-spinner-icon {}       // Targets the i tag div within stSpinner div

%sal-status {}                // Targets the stExpander root div element (st.status is named same as st.expander!)
%sal-status-summary-text {}   // Targets the summary text element (span tag, contains a p tag within markdown)
%sal-status-chevron {}        // Targets the chevron (svg tag)
%sal-status-content {}        // Targets the content div stExpanderDetails


// %sal-toast has Alternate support as it lies outside the main container.
// It can be styled directly using %%sal-toast within main.scss but does not allow custom classes

// %sal-write-stream will not be supported.
// %sal-balloons will not be supported.
// %sal-snow will not be supported.
```
