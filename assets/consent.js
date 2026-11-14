// Cookie consent (CookieConsent v3, self-hosted) with Google Consent Mode v2.
// Google Tag Manager is only loaded after the visitor accepts analytics cookies.
(function () {
  const lang = (document.documentElement.lang || "en").slice(0, 2);
  const privacy = { en: "/privacy/", de: "/de/privacy/", es: "/es/privacy/" }[lang] || "/privacy/";

  function gtag() { window.dataLayer.push(arguments); }

  function applyConsent() {
    const analytics = CookieConsent.acceptedCategory("analytics");
    gtag("consent", "update", { analytics_storage: analytics ? "granted" : "denied" });
  }

  const t = {
    en: {
      consentModal: {
        title: "Cookies, off the record",
        description: "This site uses Google Analytics to understand which episodes people read. Analytics cookies are only set if you agree. Read the <a href=\"" + privacy + "\">privacy policy</a>.",
        acceptAllBtn: "Accept",
        acceptNecessaryBtn: "Reject",
        showPreferencesBtn: "Settings",
      },
      preferencesModal: {
        title: "Cookie settings",
        acceptAllBtn: "Accept all",
        acceptNecessaryBtn: "Reject all",
        savePreferencesBtn: "Save settings",
        closeIconLabel: "Close",
        sections: [
          { title: "Necessary", description: "Stores your cookie choice. Always on.", linkedCategory: "necessary" },
          { title: "Analytics", description: "Google Analytics 4 via Google Tag Manager. Helps me see which pages are read. Only loaded with your consent.", linkedCategory: "analytics" },
          { title: "More information", description: "Details in the <a href=\"" + privacy + "\">privacy policy</a>." },
        ],
      },
    },
    de: {
      consentModal: {
        title: "Cookies, off the record",
        description: "Diese Website nutzt Google Analytics, um zu sehen, welche Folgen gelesen werden. Analyse-Cookies werden nur mit deiner Einwilligung gesetzt. Mehr in der <a href=\"" + privacy + "\">Datenschutzerklärung</a>.",
        acceptAllBtn: "Akzeptieren",
        acceptNecessaryBtn: "Ablehnen",
        showPreferencesBtn: "Einstellungen",
      },
      preferencesModal: {
        title: "Cookie-Einstellungen",
        acceptAllBtn: "Alle akzeptieren",
        acceptNecessaryBtn: "Alle ablehnen",
        savePreferencesBtn: "Einstellungen speichern",
        closeIconLabel: "Schließen",
        sections: [
          { title: "Notwendig", description: "Speichert deine Cookie-Auswahl. Immer aktiv.", linkedCategory: "necessary" },
          { title: "Analyse", description: "Google Analytics 4 über den Google Tag Manager. Zeigt, welche Seiten gelesen werden. Wird nur mit deiner Einwilligung geladen.", linkedCategory: "analytics" },
          { title: "Weitere Informationen", description: "Details in der <a href=\"" + privacy + "\">Datenschutzerklärung</a>." },
        ],
      },
    },
    es: {
      consentModal: {
        title: "Cookies, off the record",
        description: "Este sitio usa Google Analytics para saber qué episodios se leen. Las cookies de análisis solo se instalan si aceptas. Más en la <a href=\"" + privacy + "\">política de privacidad</a>.",
        acceptAllBtn: "Aceptar",
        acceptNecessaryBtn: "Rechazar",
        showPreferencesBtn: "Configuración",
      },
      preferencesModal: {
        title: "Configuración de cookies",
        acceptAllBtn: "Aceptar todo",
        acceptNecessaryBtn: "Rechazar todo",
        savePreferencesBtn: "Guardar configuración",
        closeIconLabel: "Cerrar",
        sections: [
          { title: "Necesarias", description: "Guardan tu elección de cookies. Siempre activas.", linkedCategory: "necessary" },
          { title: "Análisis", description: "Google Analytics 4 a través de Google Tag Manager. Muestra qué páginas se leen. Solo se carga con tu consentimiento.", linkedCategory: "analytics" },
          { title: "Más información", description: "Detalles en la <a href=\"" + privacy + "\">política de privacidad</a>." },
        ],
      },
    },
  };

  CookieConsent.run({
    guiOptions: {
      consentModal: { layout: "box", position: "bottom left", equalWeightButtons: true },
      preferencesModal: { layout: "box", equalWeightButtons: true },
    },
    categories: {
      necessary: { enabled: true, readOnly: true },
      analytics: {},
    },
    onConsent: applyConsent,
    onChange: applyConsent,
    language: { default: "en", autoDetect: "document", translations: t },
  });
})();
