System.register(['angular2/core', './service/Utils.service'], function(exports_1, context_1) {
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
    var core_1, Utils_service_1;
    var MinimumEditDistanceCalculatorComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (Utils_service_1_1) {
                Utils_service_1 = Utils_service_1_1;
            }],
        execute: function() {
            MinimumEditDistanceCalculatorComponent = (function () {
                function MinimumEditDistanceCalculatorComponent(_utilsService) {
                    this._utilsService = _utilsService;
                    this.string1 = '';
                    this.string2 = '';
                    this.message = '';
                    this.messageMode = 'warning';
                    this.message = 'Edit distance between these 2 strings will be calculated.';
                }
                MinimumEditDistanceCalculatorComponent.prototype.onClick = function () {
                    var _this = this;
                    this.message = '';
                    if (this.string1 === '' && this.string2 === '') {
                        this.message += 'I did not need to make the call since both strings were empty and I could easily give the result which is 0. ';
                    }
                    else if (this.string1 === '') {
                        this.message += "I did not need to make the call since the first string was empty and I could easily give the result which is " + this.string2.length + ". ";
                    }
                    else if (this.string2 === '') {
                        this.message += "I did not need to make the call since the second string was empty and I could easily give the result which is " + this.string1.length + ". ";
                    }
                    this._utilsService.getMinimumEditDistance(this.string1, this.string2).subscribe(function (data) { _this.message += "Server response is " + data.minimumEditDistance + "."; _this.messageMode = 'success'; }, function (error) { _this.message = 'Something went terribly wrong. Please try again.'; _this.messageMode = 'danger'; });
                };
                MinimumEditDistanceCalculatorComponent = __decorate([
                    core_1.Component({
                        selector: 'minimum-edit-distance-calculator',
                        templateUrl: 'partials/minimumEditDistanceCalculator.html',
                        styleUrls: ['css/minimumEditDistanceCalculator.css'],
                        providers: [Utils_service_1.UtilsService]
                    }), 
                    __metadata('design:paramtypes', [Utils_service_1.UtilsService])
                ], MinimumEditDistanceCalculatorComponent);
                return MinimumEditDistanceCalculatorComponent;
            }());
            exports_1("MinimumEditDistanceCalculatorComponent", MinimumEditDistanceCalculatorComponent);
        }
    }
});

//# sourceMappingURL=minimumEditDistanceCalculator.component.js.map
