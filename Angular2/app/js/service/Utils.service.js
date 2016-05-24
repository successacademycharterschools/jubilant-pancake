System.register(["angular2/core", 'angular2/http', 'rxjs/Rx'], function(exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, http_1;
    var UtilsService;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (_1) {}],
        execute: function() {
            UtilsService = (function () {
                function UtilsService(http) {
                    this.http = http;
                    this.api_url = "http://localhost:3000/api/1/Utils/";
                    this.http = http;
                }
                UtilsService.prototype.getMinimumEditDistance = function (string1, string2) {
                    var body = "?string1=" + string1 + "&string2=" + string2;
                    return this.http.get(this.api_url + 'minimumEditDistance' + body).map(function (res) { return res.json(); });
                };
                UtilsService = __decorate([
                    core_1.Injectable(), 
                    __metadata('design:paramtypes', [http_1.Http])
                ], UtilsService);
                return UtilsService;
            }());
            exports_1("UtilsService", UtilsService);
        }
    }
});

//# sourceMappingURL=Utils.service.js.map
