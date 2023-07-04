```php
<?php
/*
Plugin Name: AI Article Generator
Description: A plugin to generate and post AI-based articles.
Version: 1.0
Author: AI
*/

// Global variables
$plugin_id = 'ai_article_generator';
$server_address = 'http://your-server-address.com';

// Add a menu for our plugin
add_action('admin_menu', 'ai_article_generator_menu');

function ai_article_generator_menu() {
    global $plugin_id;
    add_menu_page('AI Article Generator Settings', 'AI Article Generator', 'manage_options', $plugin_id . '_settings', 'ai_article_generator_settings_page', 'dashicons-admin-generic');
}

// Create settings page
function ai_article_generator_settings_page() {
    global $plugin_id;
    ?>
    <div class="wrap">
        <h2>AI Article Generator Settings</h2>
        <form method="post" action="options.php">
            <?php settings_fields($plugin_id . '_settings'); ?>
            <?php do_settings_sections($plugin_id . '_settings'); ?>
            <table class="form-table">
                <tr valign="top">
                    <th scope="row">Server Address</th>
                    <td><input type="text" name="server_address" value="<?php echo esc_attr(get_option('server_address')); ?>" /></td>
                </tr>
            </table>
            <?php submit_button(); ?>
        </form>
    </div>
    <?php
}

// Register and define the settings
add_action('admin_init', 'ai_article_generator_admin_init');

function ai_article_generator_admin_init(){
    global $plugin_id;
    register_setting($plugin_id . '_settings', 'server_address');
}

// Add a button to generate an article
add_action('admin_footer', 'add_generate_article_button');

function add_generate_article_button() {
    ?>
    <button id="post_button" class="button button-primary button-large">Generate Article</button>
    <?php
}

?>
```