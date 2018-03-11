/* Polyfill Injector */
(function(main) {
    if(/* Intl */!('Intl' in this)) {
        var js = document.createElement('script');
        js.src = "https://d3njjcbhbojbot.cloudfront.net/web/bundles/vendor/Intl.js.v0-1-4/Intl.en-US.js?features=Intl";
        js.onload = main;
        js.onerror = function() {
            console.error('Could not load polyfills script!');
            main();
        };
        document.head.appendChild(js);
    } else {
        main();
    }
})(function() {
webpackJsonp([68],{AtUA:function(module,exports,t){"use strict";function _classCallCheck(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function getCurrentHref(){return window.location.href}function addMark(t){"undefined"!=typeof LUX&&LUX&&LUX.mark(t)}function mutationCallback(t,a){if(getCurrentHref()!==e)return void(void 0!==r&&r.destroy());var o={};t.forEach(function(t){if(t.type===i){if(!t.target.hasChildNodes())return;for(var e=t.target.firstChild;e;){if(e&&e.dataset&&e.dataset.elementtiming){var a=e.dataset.elementtiming;if(!o[a]){if(e.tagName===n){var r=new Image;r.onload=addMark.bind(null,e.dataset.elementtiming),r.src=e.src}else addMark(e.dataset.elementtiming);o[a]=!0}}e=e.nextSibling}}})}var e=getCurrentHref(),n="IMG",i="childList",a=function(){function ElementMonitor(t){_classCallCheck(this,ElementMonitor),this.onMutation=t.onMutation,this.observer=new MutationObserver(this.onMutation)}return ElementMonitor.prototype.initialize=function initialize(){this.observer.observe(document,{subtree:!0,attributes:!0,characterData:!0,childList:!0})},ElementMonitor.prototype.destroy=function destroy(){this.observer.disconnect()},ElementMonitor}(),r=new a({onMutation:mutationCallback});r.initialize()}},["AtUA"]);
});
//# sourceMappingURL=monitoring.7caeb616046c8d415c2e.js.map