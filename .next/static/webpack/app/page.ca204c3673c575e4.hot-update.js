"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
self["webpackHotUpdate_N_E"]("app/page",{

/***/ "(app-pages-browser)/./src/app/page.tsx":
/*!**************************!*\
  !*** ./src/app/page.tsx ***!
  \**************************/
/***/ (function(module, __webpack_exports__, __webpack_require__) {

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": function() { return /* binding */ Home; }\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/jsx-dev-runtime.js\");\n/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! axios */ \"(app-pages-browser)/./node_modules/axios/lib/axios.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);\n/* __next_internal_client_entry_do_not_use__ default auto */ \nvar _s = $RefreshSig$();\n\n\nfunction Home() {\n    _s();\n    const [sentence, setSentence] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(\"\");\n    const [sentiment, setSentiment] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(null);\n    async function handleSubmit(e) {\n        e.preventDefault();\n        const { data } = await axios__WEBPACK_IMPORTED_MODULE_2__[\"default\"].post(\"http://localhost:8001/calcsentiment\", {\n            sentence: sentence\n        });\n        setSentiment(data.sentiment);\n    }\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.Fragment, {\n        children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"form\", {\n            onSubmit: handleSubmit,\n            children: [\n                /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"input\", {\n                    className: \"border border-2\",\n                    type: \"text\",\n                    value: sentence,\n                    onChange: (param)=>{\n                        let { target } = param;\n                        return setSentence(target.value);\n                    }\n                }, void 0, false, {\n                    fileName: \"D:\\\\cyruz\\\\projects\\\\next\\\\clztest\\\\src\\\\app\\\\page.tsx\",\n                    lineNumber: 18,\n                    columnNumber: 9\n                }, this),\n                /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"button\", {\n                    type: \"submit\",\n                    children: \"Analyze\"\n                }, void 0, false, {\n                    fileName: \"D:\\\\cyruz\\\\projects\\\\next\\\\clztest\\\\src\\\\app\\\\page.tsx\",\n                    lineNumber: 24,\n                    columnNumber: 9\n                }, this)\n            ]\n        }, void 0, true, {\n            fileName: \"D:\\\\cyruz\\\\projects\\\\next\\\\clztest\\\\src\\\\app\\\\page.tsx\",\n            lineNumber: 17,\n            columnNumber: 7\n        }, this)\n    }, void 0, false);\n}\n_s(Home, \"orCnynF8+xhfPg7WooarZg8BBDs=\");\n_c = Home;\nvar _c;\n$RefreshReg$(_c, \"Home\");\n\n\n;\n    // Wrapped in an IIFE to avoid polluting the global scope\n    ;\n    (function () {\n        var _a, _b;\n        // Legacy CSS implementations will `eval` browser code in a Node.js context\n        // to extract CSS. For backwards compatibility, we need to check we're in a\n        // browser context before continuing.\n        if (typeof self !== 'undefined' &&\n            // AMP / No-JS mode does not inject these helpers:\n            '$RefreshHelpers$' in self) {\n            // @ts-ignore __webpack_module__ is global\n            var currentExports = module.exports;\n            // @ts-ignore __webpack_module__ is global\n            var prevSignature = (_b = (_a = module.hot.data) === null || _a === void 0 ? void 0 : _a.prevSignature) !== null && _b !== void 0 ? _b : null;\n            // This cannot happen in MainTemplate because the exports mismatch between\n            // templating and execution.\n            self.$RefreshHelpers$.registerExportsForReactRefresh(currentExports, module.id);\n            // A module can be accepted automatically based on its exports, e.g. when\n            // it is a Refresh Boundary.\n            if (self.$RefreshHelpers$.isReactRefreshBoundary(currentExports)) {\n                // Save the previous exports signature on update so we can compare the boundary\n                // signatures. We avoid saving exports themselves since it causes memory leaks (https://github.com/vercel/next.js/pull/53797)\n                module.hot.dispose(function (data) {\n                    data.prevSignature =\n                        self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports);\n                });\n                // Unconditionally accept an update to this module, we'll check if it's\n                // still a Refresh Boundary later.\n                // @ts-ignore importMeta is replaced in the loader\n                module.hot.accept();\n                // This field is set when the previous version of this module was a\n                // Refresh Boundary, letting us know we need to check for invalidation or\n                // enqueue an update.\n                if (prevSignature !== null) {\n                    // A boundary can become ineligible if its exports are incompatible\n                    // with the previous exports.\n                    //\n                    // For example, if you add/remove/change exports, we'll want to\n                    // re-execute the importing modules, and force those components to\n                    // re-render. Similarly, if you convert a class component to a\n                    // function, we want to invalidate the boundary.\n                    if (self.$RefreshHelpers$.shouldInvalidateReactRefreshBoundary(prevSignature, self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports))) {\n                        module.hot.invalidate();\n                    }\n                    else {\n                        self.$RefreshHelpers$.scheduleUpdate();\n                    }\n                }\n            }\n            else {\n                // Since we just executed the code for the module, it's possible that the\n                // new exports made it ineligible for being a boundary.\n                // We only care about the case when we were _previously_ a boundary,\n                // because we already accepted this update (accidental side effect).\n                var isNoLongerABoundary = prevSignature !== null;\n                if (isNoLongerABoundary) {\n                    module.hot.invalidate();\n                }\n            }\n        }\n    })();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwcC1wYWdlcy1icm93c2VyKS8uL3NyYy9hcHAvcGFnZS50c3giLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7OztBQUMwQjtBQUNPO0FBRWxCLFNBQVNFOztJQUN0QixNQUFNLENBQUNDLFVBQVVDLFlBQVksR0FBR0gsK0NBQVFBLENBQUM7SUFDekMsTUFBTSxDQUFDSSxXQUFXQyxhQUFhLEdBQUdMLCtDQUFRQSxDQUFDO0lBQzNDLGVBQWVNLGFBQWFDLENBQU07UUFDaENBLEVBQUVDLGNBQWM7UUFDaEIsTUFBTSxFQUFFQyxJQUFJLEVBQUUsR0FBRyxNQUFNViw2Q0FBS0EsQ0FBQ1csSUFBSSxDQUFDLHVDQUF1QztZQUN2RVIsVUFBVUE7UUFDWjtRQUNBRyxhQUFhSSxLQUFLTCxTQUFTO0lBQzdCO0lBQ0EscUJBQ0U7a0JBQ0UsNEVBQUNPO1lBQUtDLFVBQVVOOzs4QkFDZCw4REFBQ087b0JBQ0NDLFdBQVU7b0JBQ1ZDLE1BQUs7b0JBQ0xDLE9BQU9kO29CQUNQZSxVQUFVOzRCQUFDLEVBQUVDLE1BQU0sRUFBRTsrQkFBS2YsWUFBWWUsT0FBT0YsS0FBSzs7Ozs7Ozs4QkFFcEQsOERBQUNHO29CQUFPSixNQUFLOzhCQUFTOzs7Ozs7Ozs7Ozs7O0FBSTlCO0dBdkJ3QmQ7S0FBQUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9fTl9FLy4vc3JjL2FwcC9wYWdlLnRzeD9mNjhhIl0sInNvdXJjZXNDb250ZW50IjpbIlwidXNlIGNsaWVudFwiO1xuaW1wb3J0IGF4aW9zIGZyb20gXCJheGlvc1wiO1xuaW1wb3J0IHsgdXNlU3RhdGUgfSBmcm9tIFwicmVhY3RcIjtcblxuZXhwb3J0IGRlZmF1bHQgZnVuY3Rpb24gSG9tZSgpIHtcbiAgY29uc3QgW3NlbnRlbmNlLCBzZXRTZW50ZW5jZV0gPSB1c2VTdGF0ZShcIlwiKTtcbiAgY29uc3QgW3NlbnRpbWVudCwgc2V0U2VudGltZW50XSA9IHVzZVN0YXRlKG51bGwpO1xuICBhc3luYyBmdW5jdGlvbiBoYW5kbGVTdWJtaXQoZTogYW55KSB7XG4gICAgZS5wcmV2ZW50RGVmYXVsdCgpO1xuICAgIGNvbnN0IHsgZGF0YSB9ID0gYXdhaXQgYXhpb3MucG9zdChcImh0dHA6Ly9sb2NhbGhvc3Q6ODAwMS9jYWxjc2VudGltZW50XCIsIHtcbiAgICAgIHNlbnRlbmNlOiBzZW50ZW5jZSxcbiAgICB9KTtcbiAgICBzZXRTZW50aW1lbnQoZGF0YS5zZW50aW1lbnQpO1xuICB9XG4gIHJldHVybiAoXG4gICAgPD5cbiAgICAgIDxmb3JtIG9uU3VibWl0PXtoYW5kbGVTdWJtaXR9PlxuICAgICAgICA8aW5wdXRcbiAgICAgICAgICBjbGFzc05hbWU9XCJib3JkZXIgYm9yZGVyLTJcIlxuICAgICAgICAgIHR5cGU9XCJ0ZXh0XCJcbiAgICAgICAgICB2YWx1ZT17c2VudGVuY2V9XG4gICAgICAgICAgb25DaGFuZ2U9eyh7IHRhcmdldCB9KSA9PiBzZXRTZW50ZW5jZSh0YXJnZXQudmFsdWUpfVxuICAgICAgICAvPlxuICAgICAgICA8YnV0dG9uIHR5cGU9XCJzdWJtaXRcIj5BbmFseXplPC9idXR0b24+XG4gICAgICA8L2Zvcm0+XG4gICAgPC8+XG4gICk7XG59XG4iXSwibmFtZXMiOlsiYXhpb3MiLCJ1c2VTdGF0ZSIsIkhvbWUiLCJzZW50ZW5jZSIsInNldFNlbnRlbmNlIiwic2VudGltZW50Iiwic2V0U2VudGltZW50IiwiaGFuZGxlU3VibWl0IiwiZSIsInByZXZlbnREZWZhdWx0IiwiZGF0YSIsInBvc3QiLCJmb3JtIiwib25TdWJtaXQiLCJpbnB1dCIsImNsYXNzTmFtZSIsInR5cGUiLCJ2YWx1ZSIsIm9uQ2hhbmdlIiwidGFyZ2V0IiwiYnV0dG9uIl0sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///(app-pages-browser)/./src/app/page.tsx\n"));

/***/ })

});