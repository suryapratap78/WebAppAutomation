class BsidcaSoapBodies:
    connectApi_body = """<?xml version="1.0" encoding="UTF-8"?>
             <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:blac="http://www.cryptocard.com/blackshield/">
       <soap:Header/>
       <soap:Body>
          <blac:Connect>
             <!--Optional:-->
             <blac:OperatorEmail>{}</blac:OperatorEmail>
             <!--Optional:-->
             <blac:OTP>{}</blac:OTP>
             <!--Optional:-->
             <blac:validationCode>?</blac:validationCode>
          </blac:Connect>
       </soap:Body>
    </soap:Envelope>"""


    testsadsa = """dsfgrefgdjn"""

    addGroupApi_body = """<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:blac="http://www.cryptocard.com/blackshield/">
       <soap:Header/>
       <soap:Body>
          <blac:AddGroup>
             <!--Optional:-->
             <blac:groupName>{}</blac:groupName>
             <!--Optional:-->
             <blac:description></blac:description>
             <!--Optional:-->
             <blac:organization>{}</blac:organization>
          </blac:AddGroup>
       </soap:Body>
    </soap:Envelope>"""

    addUserApi_body = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:blac="http://www.cryptocard.com/blackshield/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
   <soap:Header/>
   <soap:Body>
      <blac:AddUser>
         <!--Optional:-->
         <blac:user>
            <blac:RestrictionsEnabled>false</blac:RestrictionsEnabled>
            <blac:PreferredLanguage xsi:nil="true"></blac:PreferredLanguage>
            <!--Optional:-->
            <blac:UserName>{}</blac:UserName>
            <!--Optional:-->
            <blac:FirstName>{}</blac:FirstName>
             <!--Optional:-->
            <blac:Email>{}@ymail.com</blac:Email>
            <blac:Locked>false</blac:Locked>
            <blac:TempPasswordEnabled>false</blac:TempPasswordEnabled>
            <blac:TempPasswordChangeReq>false</blac:TempPasswordChangeReq>
            <blac:UseExternalCredentials>false</blac:UseExternalCredentials>
            <blac:IsAccountDormant>false</blac:IsAccountDormant>
         </blac:user>
         <!--Optional:-->
         <blac:organization>{}</blac:organization>
      </blac:AddUser>
   </soap:Body>
</soap:Envelope>"""

    addAccountApi_body = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:blac="http://www.cryptocard.com/blackshield/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
   <soap:Header/>
   <soap:Body>
      <blac:AddOrganization>
         <!--Optional:-->
         <blac:organization>
            <blac:AccountActive>true</blac:AccountActive>
            <blac:EvaluationAccount>false</blac:EvaluationAccount>
            <blac:_oldAccountType>ServiceProvider</blac:_oldAccountType>
            <blac:_currentAccountType>ServiceProvider</blac:_currentAccountType>
            <blac:StartDate>2020-04-01T00:00:00</blac:StartDate>
            <blac:EndDate>2023-04-01T00:00:00</blac:EndDate>
            <blac:billingType>Monthly</blac:billingType>
            <blac:AuthNodeCount>10</blac:AuthNodeCount>
            <blac:AllowedThirdPartyTokens>false</blac:AllowedThirdPartyTokens>
            <blac:Capacity>0</blac:Capacity>
            <blac:IceCapacity>0</blac:IceCapacity>
            <blac:Delegated>false</blac:Delegated>
            <blac:SMSCredits>0</blac:SMSCredits>
            <blac:SMSSent>0</blac:SMSSent>
            <blac:SMSAlertLevel>0</blac:SMSAlertLevel>
            <blac:LanguageHasChanged>true</blac:LanguageHasChanged>
            <blac:SelfServiceLanguage>0</blac:SelfServiceLanguage>
            <blac:InheritMailMessages>true</blac:InheritMailMessages>
            <blac:InheritSMSMessages>true</blac:InheritSMSMessages>
            <blac:InheritCustomizations>true</blac:InheritCustomizations>
            <blac:InheritLDAPSyncServerSettings>false</blac:InheritLDAPSyncServerSettings>
            <blac:InheritRADIUSServerSettings>true</blac:InheritRADIUSServerSettings>
            <blac:InheritDocumentURL>true</blac:InheritDocumentURL>
            <blac:InheritAgentURL>true</blac:InheritAgentURL>
            <blac:InheritTermsOfUse>true</blac:InheritTermsOfUse>
            <blac:InheritAgentDNS>true</blac:InheritAgentDNS>
            <blac:InheritServiceNotifications>true</blac:InheritServiceNotifications>
            <blac:InheritSAMLDetails>true</blac:InheritSAMLDetails>            	  <blac:InheritSelfServiceCustomizations>true</blac:InheritSelfServiceCustomizations>
            <blac:InheritLoggingAgentSettings>true</blac:InheritLoggingAgentSettings>
            <blac:UseHelpDesk>false</blac:UseHelpDesk>
            <blac:GenerateEvents>true</blac:GenerateEvents>
            <blac:SAEEnable>false</blac:SAEEnable>
            <blac:TimeOffSetQH>0</blac:TimeOffSetQH>
            <blac:orgName>{}</blac:orgName>
            <blac:accountType>ServiceProvider</blac:accountType>
            <blac:Language>0</blac:Language>
            <blac:UseDelayedSyncRemoval>false</blac:UseDelayedSyncRemoval>
            <blac:PersistOperatorsAgainstSync>true</blac:PersistOperatorsAgainstSync>
            <blac:UseLocalSync>false</blac:UseLocalSync>
            <blac:AllowNonSyncUsers>true</blac:AllowNonSyncUsers>
            <blac:LocalSyncIdleTimeInSeconds>300</blac:LocalSyncIdleTimeInSeconds>
            <blac:StripSyncCharacters>false</blac:StripSyncCharacters>
            <blac:SyncHistoryPerHost>100</blac:SyncHistoryPerHost>
            <blac:ReportAutoRemoveDayCount>365</blac:ReportAutoRemoveDayCount>
            <blac:AccountReportAutoRemoveDayCount>365</blac:AccountReportAutoRemoveDayCount>
            <blac:AlertAutoRemoveDayCount>0</blac:AlertAutoRemoveDayCount>
            <blac:CreatedDate>2020-04-01T09:48:00.1830000+00:00</blac:CreatedDate>
         </blac:organization>
         
      </blac:AddOrganization>
   </soap:Body>
</soap:Envelope>"""