function init_widgets_for_htmx_element(target) {
    // init other widgets

    // init modal dialogs
    if (target.tagName === 'DIALOG') {
        target.showModal();
        htmx.on(".close-dialog", "click", function(event) {
            var dialog = htmx.find('dialog[open]');
            dialog.close();
            htmx.remove(dialog);
        });
    }
}

htmx.onLoad(init_widgets_for_htmx_element);
